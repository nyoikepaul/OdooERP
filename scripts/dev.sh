#!/bin/bash
set -e
echo ">>> Starting OdooERP Kenya (dev)..."
[ ! -f .env ] && cp .env.example .env && echo "⚠ .env created — fill in passwords before proceeding" && exit 1
docker compose up -d
echo ">>> ONLINE: http://localhost:8069"
docker compose logs -f web
