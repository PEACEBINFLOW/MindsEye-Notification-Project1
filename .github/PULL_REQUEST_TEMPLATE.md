## Summary
<!-- What does this PR change? Why? -->

## Changes
- [ ] Code
- [ ] Docs
- [ ] Config
- [ ] Tests (n/a for this repo)

## How to Test
1. `pip install -r requirements.txt`
2. Ensure `.env` is *not* committed. Use `.env.example` to configure locally.
3. Run: `python mindseye_email.py`

## Checklist
- [ ] No secrets committed (`.env`, creds, tokens)
- [ ] `template.json` has `template_name`, `subject`, `body`
- [ ] `config.json` has `notification_settings`
- [ ] CI is passing
