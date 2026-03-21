# Odoo ERP Prowess — Paul Nyoike (Nairobi, Kenya)

**Production-ready Odoo custom modules that African businesses actually use.**

I deliver **full-cycle Odoo solutions** — from requirements to live deployment — for real-estate, fintech, retail, and manufacturing in Kenya, Ghana, Uganda & East Africa.

### Live Demo & Screenshots
(Upload 4-5 screenshots of your modules here — Odoo dashboard, M-Pesa STK push, real-estate property card, agent portal, KRA-ready invoice)

### Featured Modules

#### 1. Ghana Real Estate ERP (Odoo 16) — [View Code](https://github.com/nyoikepaul/Odoo) (already live)
- Property CRM + 200+ properties managed 100% inside Odoo  
- Agent portal & client inquiry workflow  
- GHS pricing & multi-currency  
- M-Pesa ready + responsive website (Tailwind + QWeb)  
- Client testimonial: “We replaced 3 separate tools with one Odoo instance”

#### 2. Kenya M-Pesa Payment Acquirer (Odoo 17/18) — **New in this repo** (coming in next commit)
- Full STK Push, C2B, B2C, Reversal & Confirmation webhooks  
- Automatic invoice reconciliation  
- Kenyan tax (KRA) handling & eTIMS-ready invoices  
- Works with Sales, POS, eCommerce & Invoicing

#### 3. Advanced Features Demonstrated (prowess proof)
- Model inheritance & delegation  
- Computed fields + @api.depends  
- Wizards, scheduled actions & automated workflows  
- Custom payment provider (payment_acquirer base)  
- REST API controllers + webhook security  
- QWeb reports + PDF customization  
- Multi-company, multi-currency, multi-language  
- Docker + GitHub Actions CI/CD  
- Full security groups & record rules

### Tech Stack
- **Odoo** 16 / 17 / 18 (Enterprise-ready code)  
- **Python** 3.10+ | PostgreSQL | Nginx  
- **M-Pesa** Daraja API (STK Push + callbacks)  
- **Docker** + **docker-compose** (one-click dev environment)  
- **Tailwind CSS** + **QWeb** for beautiful frontends

### Quick Start (Local Demo in 60 seconds)

```bash
git clone https://github.com/nyoikepaul/odoo-erp-prowess.git
cd odoo-erp-prowess
docker compose up -d
# Open http://localhost:8069 → login: admin / admin
# Install "Kenya M-Pesa Payment" module
