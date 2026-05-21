# Kenya Real Estate CRM

Manage properties, tenants, leases and rent invoicing — built for the Kenyan market.

## Features
- Property listings with status tracking (Available, Leased, For Sale, Sold)
- Tenant lease management with start/end dates
- One-click rent invoice generation
- M-Pesa rent collection via `kenya_mpesa_acquirer`
- Auto-generated refs: `PROP/2026/0001`, `LEASE/2026/0001`

## Installation
Requires: `mpesa_connector`, `account`, `mail`

## Models
- `estate.property` — Property listings
- `estate.lease` — Tenancy agreements
