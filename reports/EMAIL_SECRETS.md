# Email Secrets Configuration

## ✅ Required Secrets

Add these to: **https://github.com/berlogabob/Project02/settings/secrets/actions**

---

### Already Added ✅

| Secret Name | Value | Status |
|-------------|-------|--------|
| `EMAIL_USERNAME` | `andre.berloga@gmail.com` | ✅ Added |
| `EMAIL_PASSWORD` | `vkws wxyg lkmn tnah` | ✅ Added |

---

### Still Need to Add ⏳

| Secret Name | Value | Click |
|-------------|-------|-------|
| `EMAIL_TO_ANDREY` | `berloga.bob@gmail.com` | [Add Secret](https://github.com/berlogabob/Project02/settings/secrets/actions/new) |
| `EMAIL_TO_NADINE` | `[Nadine's email]` | [Add Secret](https://github.com/berlogabob/Project02/settings/secrets/actions/new) |
| `EMAIL_TO_DMITRI` | `[Dmitri's email]` | [Add Secret](https://github.com/berlogabob/Project02/settings/secrets/actions/new) |

---

## 📝 Quick Add Instructions

### 1. Add Your Email

1. Click: **https://github.com/berlogabob/Project02/settings/secrets/actions/new**
2. **Name:** `EMAIL_TO_ANDREY`
3. **Value:** `berloga.bob@gmail.com`
4. Click **Add secret**

### 2. Add Nadine's Email

1. Click: **https://github.com/berlogabob/Project02/settings/secrets/actions/new**
2. **Name:** `EMAIL_TO_NADINE`
3. **Value:** `[Ask Nadine for her email]`
4. Click **Add secret**

### 3. Add Dmitri's Email

1. Click: **https://github.com/berlogabob/Project02/settings/secrets/actions/new**
2. **Name:** `EMAIL_TO_DMITRI`
3. **Value:** `[Ask Dmitri for his email]`
4. Click **Add secret**

---

## ✅ After Adding All Secrets

### Test the Workflow

1. Go to: **https://github.com/berlogabob/Project02/actions/workflows/daily-plans-v2.yml**
2. Click **"Run workflow"**
3. Select branch: `main`
4. Click **"Run workflow"**
5. Wait 3 minutes
6. Check your email: `berloga.bob@gmail.com`

---

## 📧 What You'll Receive

**Subject:**
```
📅 Daily Plan - 2026-03-05 - The Oracle That Wears Us
```

**Email will contain:**
- ✅ Your personalized daily plan PDF
- ✅ Links to all team member plans
- ✅ Instructions on how to use
- ✅ Direct links to repository

---

## 🔍 Verify All Secrets

Go to: **https://github.com/berlogabob/Project02/settings/secrets/actions**

You should see:

```
EMAIL_USERNAME          (andre.berloga@gmail.com)
EMAIL_PASSWORD          (vkws...tnah)
EMAIL_TO_ANDREY         (berloga.bob@gmail.com)
EMAIL_TO_NADINE         ([Nadine's email])
EMAIL_TO_DMITRI         ([Dmitri's email])
```

---

## ⏰ Automatic Schedule

After testing, emails will be sent automatically:
- **Every day at 00:00 UTC** (02:00 Lisbon time)
- **To all 3 team members**
- **With PDFs attached**

---

**Next:** Add the 3 remaining secrets and test! 🚀
