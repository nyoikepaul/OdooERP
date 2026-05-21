# Contributing to OdooERP Kenya

## Setup
```bash
git clone https://github.com/NyoikePaul/OdooERP.git
cd OdooERP
cp .env.example .env
docker compose up -d
```

## Module Development
- Place custom modules in `custom_addons/`
- Follow Odoo 18 module structure
- All models must have `ir.model.access.csv` security entries
- Use `mail.thread` + `mail.activity.mixin` for business models

## Commit Convention
- `feat:` new feature
- `fix:` bug fix
- `docs:` documentation
- `test:` adding tests
- `ci:` CI/CD changes

## Testing
```bash
docker compose exec web python odoo-bin -d odoo --test-enable \
  --stop-after-init -i kenya_real_estate
```
