# Email Notification Setup Guide

## 🔧 Configure Email Notifications

### Step 1: Get Email Credentials

#### Option A: Gmail (Recommended)

1. **Enable 2FA** on your Google account
2. **Generate App Password:**
   - Go to: https://myaccount.google.com/apppasswords
   - Select "Mail" and your device
   - Copy the 16-character password

#### Option B: SendGrid (Free, Professional)

1. Sign up: https://sendgrid.com/
2. Verify email
3. Create API Key:
   - Settings → API Keys → Create API Key
   - Full Access
   - Copy the key

---

### Step 2: Add GitHub Secrets

Go to: **https://github.com/berlogabob/Project02/settings/secrets/actions**

Add these secrets:

| Secret Name | Value | Example |
|-------------|-------|---------|
| `EMAIL_USERNAME` | Your email address | `yourname@gmail.com` |
| `EMAIL_PASSWORD` | App password or API key | `abcd1234efgh5678` |
| `EMAIL_TO_NADINE` | Nadine's email | `nadine.allan@university.edu` |
| `EMAIL_TO_ANDREY` | Andrey's email | `andrey.dyakov@university.edu` |
| `EMAIL_TO_DMITRI` | Dmitri's email | `dmitri.kazantsev@university.edu` |

---

### Step 3: Update Team Emails

Edit `.github/workflows/daily-plans-v2.yml`:

```yaml
- name: Send email notifications
  uses: dawidd6/action-send-mail@v3
  with:
    # ...
    to: |
      ${{ secrets.EMAIL_TO_NADINE }},
      ${{ secrets.EMAIL_TO_ANDREY }},
      ${{ secrets.EMAIL_TO_DMITRI }}
```

---

### Step 4: Test Email

Manually trigger the workflow:

1. Go to: **https://github.com/berlogabob/Project02/actions/workflows/daily-plans-v2.yml**
2. Click **"Run workflow"**
3. Select branch: `main`
4. Click **"Run workflow"**
5. Wait 2-3 minutes
6. Check email inbox!

---

## 📧 Email Template Preview

**Subject:** 📅 Daily Plan - 2026-03-05 - The Oracle That Wears Us

**Body:**

```
📅 Daily Plans Generated - 2026-03-05

Your personalized daily plan is ready!

Team Member Plans:
┌──────────────────┬───────────────┬────────┐
│ Member           │ Plan PDF      │ Issues │
├──────────────────┼───────────────┼────────┤
│ Nadine Allan     │ Download PDF  │ See PDF│
│ Andrey Dyakov    │ Download PDF  │ See PDF│
│ Dmitri Kazantsev │ Download PDF  │ See PDF│
└──────────────────┴───────────────┴────────┘

How to Use Your Daily Plan:
1. Download your personalized PDF
2. Review your assigned tasks
3. Check sub-issues and recent comments
4. Plan your time blocks
5. Update issues as you work
6. Comment your progress

Direct Links:
- All Plans: [link]
- Workflow Runs: [link]

Auto-generated every day at 00:00 UTC (02:00 Lisbon)

Today's Focus: Make progress on your assigned issues and 
update the team! 💪
```

---

## ✅ Verify Email Works

After first run, check:

1. **Inbox** - Should receive email
2. **Spam** - Sometimes goes there initially
3. **GitHub Actions** - Look for green checkmark

---

## 🔧 Troubleshooting

### Email Not Received?

1. **Check spam folder**
2. **Verify secrets** are correct
3. **Check workflow logs** for errors
4. **Test with personal email** first

### Gmail Issues?

- Ensure **App Password** (not regular password)
- Check **2FA is enabled**
- Verify **less secure apps** setting

### SendGrid Issues?

- Verify **API Key** has full access
- Check **sender email** is verified
- Review **SendGrid dashboard** for errors

---

## 🎯 Alternative: GitHub Notifications Only

If email is too complex, team can:

1. **Watch repository** → Get email on every commit
2. **Use GitHub Mobile** → Push notifications
3. **Check daily** → https://github.com/berlogabob/Project02/tree/main/reports/daily-plans

---

## 📊 Current Status

| Feature | Status |
|---------|--------|
| Generate TYP files | ✅ Working |
| Generate PDF files | ⚠️ Testing |
| Commit to repo | ✅ Working |
| Upload artifacts | ✅ Working |
| Email notifications | ⏳ Needs setup |

---

**Next:** Add team email addresses and test! 📧
