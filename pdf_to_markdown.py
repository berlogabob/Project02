import glob
import os
import tempfile
from pathlib import Path

import ollama
from pdf2image import convert_from_path
from PIL import Image

PROMPT = "Extract all text from this image. Return the text as clean markdown."


def ocr_single_image(image_path: str) -> str:
    try:
        response = ollama.chat(
            model="qwen3.5:2b",
            messages=[
                {
                    "role": "user",
                    "content": PROMPT,
                    "images": [image_path],
                }
            ],
        )
        md_text = response["message"]["content"].strip()
        return md_text if md_text and not md_text.isspace() else ""
    except Exception as e:
        print(f"   ! OCR Error: {e}")
        return ""


def pdf_to_markdown(pdf_path: str, output_dir: str):
    base_name = Path(pdf_path).stem
    folder_path = os.path.join(output_dir, base_name)
    os.makedirs(folder_path, exist_ok=True)

    try:
        images = convert_from_path(pdf_path, dpi=150, fmt="png")
    except Exception as e:
        print(f"   ! PDF conversion error: {e}")
        return

    print(f"   Converting {len(images)} pages...")

    for i, pil_image in enumerate(images, 1):
        new_height = 640  # old was 1024
        new_width = int(new_height * pil_image.width / pil_image.height)
        pil_image = pil_image.resize((new_width, new_height), Image.Resampling.LANCZOS)

        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_img = os.path.join(tmp_dir, f"page_{i}.png")
            pil_image.save(tmp_img, "PNG")

            print(f"   Processing page {i}/{len(images)}...")
            md_text = ocr_single_image(tmp_img)

            output_file = os.path.join(folder_path, f"page_{i}.md")
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(md_text)
            print(f"   Created: {output_file}")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_files = glob.glob(os.path.join(script_dir, "*.pdf"))

    if not pdf_files:
        print("No PDF files found in the script directory.")
        return

    output_dir = script_dir

    print(f"Found {len(pdf_files)} PDF file(s)")

    for pdf_file in pdf_files:
        print(f"Processing: {pdf_file}")
        pdf_to_markdown(pdf_file, output_dir)

    print("Done!")


if __name__ == "__main__":
    main()
