import json
import os
import shutil
import tempfile
import time
from datetime import datetime
from pathlib import Path

import ollama
from pdf2image import convert_from_path
from pdf2image.exceptions import PDFInfoNotInstalledError
from PIL import Image
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# ─── Настройки ───────────────────────────────────────────────────────────────

WATCH_DIR = Path.cwd()  # папка, за которой следим
OUTPUT_DIR = Path("./output/")  # для Markdown
PROCESSED_DIR = Path("./processed/")  # для перемещённых обработанных файлов
PROCESSED_LOG = "processed.json"

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".PNG", ".JPG", ".JPEG"}
PDF_EXTS = {".pdf", ".PDF"}

OUTPUT_DIR.mkdir(exist_ok=True)
PROCESSED_DIR.mkdir(exist_ok=True)

# Если Poppler не в PATH — укажи путь здесь (редко нужно на macOS с Homebrew)
POPPLER_PATH = None

# ─── Работа с логом processed.json ──────────────────────────────────────────


def load_processed() -> dict:
    if os.path.exists(PROCESSED_LOG):
        with open(PROCESSED_LOG, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"processed": {}, "stats": {"total": 0, "by_date": {}}}


def save_processed(data: dict):
    with open(PROCESSED_LOG, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def mark_as_processed(
    file_path: Path,
    status: str = "success",
    text: str | None = None,
    page_count: int | None = None,
):
    data = load_processed()
    rel_path = str(file_path.relative_to(WATCH_DIR))
    now = datetime.now().isoformat()

    entry = {"processed_at": now, "status": status, "md_file": f"{file_path.stem}.md"}
    if text:
        entry["text"] = text
    if page_count is not None:
        entry["pages"] = page_count

    data["processed"][rel_path] = entry

    date_key = now[:10]
    data["stats"]["total"] = data["stats"].get("total", 0) + 1
    data["stats"]["by_date"][date_key] = data["stats"]["by_date"].get(date_key, 0) + 1

    save_processed(data)


def is_already_processed(file_path: Path) -> bool:
    data = load_processed()
    rel_path = str(file_path.relative_to(WATCH_DIR))
    return (
        rel_path in data["processed"]
        and data["processed"][rel_path]["status"] == "success"
    )


# ─── Обработка одного изображения ───────────────────────────────────────────


def ocr_single_image(image_path: Path | str) -> str:
    """Отправляет одно изображение в модель и возвращает Markdown"""
    try:
        response = ollama.chat(
            model="glm-ocr",  # ← можно сменить на "deepseek-ocr"
            messages=[
                {
                    "role": "user",
                    "content": (
                        "Figure Recognition: "
                        "You are a pure Markdown OCR engine. "
                        "Output the entire content of the image as clean, semantic Markdown. "
                        "Rules you MUST follow:"
                        "1. Tables → ONLY Markdown tables: | header | header | \n|--------|--------|\n| cell   | cell   | "
                        "2. Absolutely NO HTML: no <table>, no <div>, no <p>, no <b>, nothing. "
                        "3. Headings: use # for level 1, ## for level 2, etc. "
                        "4. Lists: use - or * for bullets, 1. 2. for numbered "
                        "5. Bold: **text**, italic: *text* "
                        "6. No extra text, no introductions, no Here is the result, no fences ```markdown "
                        "Output ONLY valid Markdown content starting from the first heading or paragraph."
                    ),
                    "images": [str(image_path)],
                }
            ],
        )
        md_text = response["message"]["content"].strip()
        return md_text if md_text and not md_text.isspace() else ""

    except Exception as e:
        print(f"   ! Ошибка OCR: {e}")
        return ""


# ─── Обработка файла (image или pdf) ────────────────────────────────────────


def process_file(file_path: Path):
    if is_already_processed(file_path):
        print(f"   — уже обработан → пропускаем ({file_path.name})")
        return

    print(f"→ {file_path.name}")

    try:
        full_text_parts = []
        page_count = 0

        if file_path.suffix.lower() in PDF_EXTS:
            # ─── PDF ────────────────────────────────────────────────────────
            try:
                images = convert_from_path(
                    str(file_path),
                    dpi=150,  # снижено для скорости и стабильности
                    fmt="png",
                    paths_only=False,
                    poppler_path=POPPLER_PATH if POPPLER_PATH else None,
                )
            except PDFInfoNotInstalledError:
                print(
                    "   ! Poppler не найден! Установите poppler-utils или укажите POPPLER_PATH"
                )
                mark_as_processed(file_path, "error: poppler not installed")
                return
            except Exception as e:
                print(f"   ! Ошибка конвертации PDF: {e}")
                mark_as_processed(file_path, f"error: {str(e)}")
                return

            page_count = len(images)

            with tempfile.TemporaryDirectory() as tmp_dir:
                tmp_path = Path(tmp_dir)

                for i, pil_image in enumerate(images, 1):
                    # Ресайз до ширины 1024 пикселей с сохранением пропорций
                    new_width = 1024
                    new_height = int(new_width * pil_image.height / pil_image.width)
                    pil_image = pil_image.resize(
                        (new_width, new_height), Image.Resampling.LANCZOS
                    )

                    tmp_img = tmp_path / f"page_{i}.png"
                    pil_image.save(tmp_img, "PNG")

                    print(
                        f"   Страница {i}/{page_count} (ресайз {new_width}×{new_height})..."
                    )
                    md_page = ocr_single_image(tmp_img)

                    if md_page:
                        if i == 1:
                            full_text_parts.append(md_page)
                        else:
                            full_text_parts.append(f"\n\n# Page {i}\n\n" + md_page)
                    else:
                        full_text_parts.append(
                            f"\n\n# Page {i}\n(пустая или не распознана)"
                        )

        else:
            # ─── Обычное изображение ───────────────────────────────────────
            # Можно тоже ресайзить, если хочешь унифицировать
            md_text = ocr_single_image(file_path)
            full_text_parts.append(md_text)
            page_count = 1

        if not any(full_text_parts):
            print("   ! Полностью пустой результат")
            mark_as_processed(file_path, "empty_response")
            return

        full_md = "\n\n".join(full_text_parts).strip()

        md_path = OUTPUT_DIR / f"{file_path.stem}.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(full_md)

        print(f"   ✓ {md_path.name}  ({page_count} страниц/изображений)")
        mark_as_processed(file_path, "success", full_md, page_count)

        # ─── Перемещение в processed после успеха ───────────────────────
        target_path = PROCESSED_DIR / file_path.name
        shutil.move(str(file_path), str(target_path))
        print(f"   → Перемещён в {target_path}")

    except Exception as e:
        print(f"   ✗ Ошибка: {e}")
        mark_as_processed(file_path, f"error: {str(e)}")


# ─── Watchdog handler ───────────────────────────────────────────────────────


class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        path = Path(event.src_path)
        if path.suffix.lower() not in (IMAGE_EXTS | PDF_EXTS):
            return
        time.sleep(3)  # ждём завершения записи файла
        if path.exists() and path.stat().st_size > 0:
            process_file(path)

    def on_moved(self, event):
        if event.is_directory:
            return
        path = Path(event.dest_path)
        if path.suffix.lower() not in (IMAGE_EXTS | PDF_EXTS):
            return
        time.sleep(3)
        if path.exists() and path.stat().st_size > 0:
            process_file(path)


# ─── Основная логика ────────────────────────────────────────────────────────


def main():
    data = load_processed()
    print(f"Загружено обработанных файлов: {len(data['processed'])}")
    print(f"Всего обработано: {data['stats'].get('total', 0)}\n")

    print("Проверяем существующие файлы в папке...\n")
    for file in sorted(os.listdir(WATCH_DIR)):
        path = WATCH_DIR / file
        if path.is_file() and path.suffix.lower() in (IMAGE_EXTS | PDF_EXTS):
            process_file(path)

    print("\nНачальная обработка завершена.")
    print(f"Следим за новыми файлами (img/pdf) в: {WATCH_DIR.absolute()}")
    print("   Выход → Ctrl+C\n")

    event_handler = NewFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=str(WATCH_DIR), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nОстановка наблюдения...")
    observer.join()


if __name__ == "__main__":
    main()
