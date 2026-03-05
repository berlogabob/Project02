# Daily Plans v2 - PDF + Email Notifications

## ✅ What's New in v2

| Feature | v1 | v2 |
|---------|----|----|
| Generate TYP files | ✅ | ✅ |
| Generate PDF files | ❌ | ✅ |
| Commit to repo | ✅ | ✅ |
| Upload artifacts | ✅ | ✅ |
| Email notifications | ❌ | ✅ |

---

## 🚀 Setup Instructions

### Step 1: Configure Email Secrets

Go to: **https://github.com/berlogabob/Project02/settings/secrets/actions**

Add these secrets:

```
EMAIL_USERNAME = your-email@gmail.com
EMAIL_PASSWORD = your-app-password
EMAIL_TO_NADINE = nadine.allan@university.edu
EMAIL_TO_ANDREY = andrey.dyakov@university.edu
EMAIL_TO_DMITRI = dmitri.kazantsev@university.edu
```

**See:** [EMAIL_SETUP.md](reports/EMAIL_SETUP.md) for detailed instructions

---

### Step 2: Enable v2 Workflow

1. Go to: **https://github.com/berlogabob/Project02/actions/workflows/daily-plans-v2.yml**
2. Click **"Enable workflow"** (if not already enabled)
3. Click **"Run workflow"** to test manually
4. Wait 2-3 minutes
5. Check:
   - ✅ Green checkmark in Actions
   - ✅ PDFs in `reports/daily-plans/`
   - ✅ Emails received by team

---

## 📊 Where to Find Reports

### 1. PDF Files in Repository

**Direct links:**
- [All PDFs](https://github.com/berlogabob/Project02/tree/main/reports/daily-plans)
- [Nadine's Plan](https://github.com/berlogabob/Project02/blob/main/reports/daily-plans/daily-plan-naydino.pdf)
- [Andrey's Plan](https://github.com/berlogabob/Project02/blob/main/reports/daily-plans/daily-plan-berlogabob.pdf)
- [Dmitri's Plan](https://github.com/berlogabob/Project02/blob/main/reports/daily-plans/daily-plan-electricianv001.pdf)

### 2. Email Notification

Each team member receives:
- **Subject:** 📅 Daily Plan - YYYY-MM-DD - The Oracle That Wears Us
- **Body:** HTML email with table and download links
- **To:** Their personal email address

### 3. GitHub Artifacts

1. Go to: **https://github.com/berlogabob/Project02/actions**
2. Click latest "Generate Daily Plans v2" run
3. Scroll to **Artifacts** section
4. Download:
   - `daily-plans-pdf-YYYY-MM-DD.zip` (PDFs)
   - `daily-plans-source-YYYY-MM-DD.zip` (TYP sources)

---

## 📧 Email Template

**Subject:**
```
📅 Daily Plan - 2026-03-05 - The Oracle That Wears Us
```

**Preview:**
```html
<h2>📅 Daily Plans Generated - 2026-03-05</h2>

<p>Your personalized daily plan is ready!</p>

<h3>Team Member Plans:</h3>
<table>
  <tr>
    <th>Member</th>
    <th>Plan PDF</th>
    <th>Issues</th>
  </tr>
  <tr>
    <td>Nadine Allan</td>
    <td><a href="...">Download PDF</a></td>
    <td>See PDF</td>
  </tr>
  <tr>
    <td>Andrey Dyakov</td>
    <td><a href="...">Download PDF</a></td>
    <td>See PDF</td>
  </tr>
  <tr>
    <td>Dmitri Kazantsev</td>
    <td><a href="...">Download PDF</a></td>
    <td>See PDF</td>
  </tr>
</table>
```

---

## ⏰ Schedule

| Time (UTC) | Time (Lisbon) | Event |
|------------|---------------|-------|
| **00:00** | 02:00 | Daily plans generated |
| **00:02** | 02:02 | PDFs compiled |
| **00:03** | 02:03 | Committed to repo |
| **00:04** | 02:04 | Emails sent |
| **Morning** | Morning | Team receives plans |

---

## 🧪 Test Now

```bash
# Manual trigger (no need to wait for midnight)
# Go to: https://github.com/berlogabob/Project02/actions/workflows/daily-plans-v2.yml
# Click "Run workflow"
```

Or via CLI:
```bash
gh workflow run daily-plans-v2.yml
```

---

## ✅ Checklist

- [ ] Add email secrets to GitHub
- [ ] Update team email addresses
- [ ] Test workflow manually
- [ ] Verify PDFs generated
- [ ] Check emails received
- [ ] Share access links with team
- [ ] Enable automatic schedule (already set)

---

## 🎯 Migration from v1

**v1 workflow** (`daily-plans.yml`):
- Still active
- Generates TYP files only
- No PDFs, no emails

**v2 workflow** (`daily-plans-v2.yml`):
- New, recommended
- Generates PDFs
- Sends emails
- Same schedule (00:00 UTC)

**To switch completely:**
1. Test v2 thoroughly
2. Disable v1: Actions → daily-plans.yml → ⋮ → Disable
3. Keep both running if needed (no conflict)

---

## 📊 Current Status

| Component | Status | Notes |
|-----------|--------|-------|
| TYP Generation | ✅ Working | Tested successfully |
| PDF Compilation | ⚠️ Testing | Depends on template |
| Email Sending | ⏳ Pending | Needs secrets |
| Artifacts Upload | ✅ Working | Both PDF + TYP |
| Auto Schedule | ✅ Active | 00:00 UTC daily |

---

## 🔧 Troubleshooting

### PDFs Not Generated?

Check workflow logs:
```
Run Compile PDFs
Compiling daily-plan-naydino.typ -> daily-plan-naydino.pdf
Warning: Failed to compile daily-plan-naydino.typ
```

**Solution:** Fix Typst template errors

### Emails Not Received?

1. Check spam folder
2. Verify secrets are correct
3. Check workflow logs for errors
4. Test with personal email first

### Template Errors?

Review `reports/daily-plan-template.typ` for syntax issues

---

## 📞 Team Instructions

**Share this with your team:**

```
📅 Daily Plans - How to Access

Starting today, you'll receive a daily email at 02:00 Lisbon time
with your personalized task plan.

1. Check your email every morning
2. Download your PDF
3. Review your tasks
4. Plan your day
5. Update issues as you work

Can't find the email?
→ Check spam folder
→ Add GitHub Actions to contacts
→ Access directly: https://github.com/berlogabob/Project02/tree/main/reports/daily-plans

Questions? Ask Andrey!
```

---

**Created:** March 5, 2026  
**Version:** 2.0  
**Status:** Ready for testing 🚀
