#!/bin/bash
echo ">>> STAGING ODOO_ERP_KERNEL..."
docker-compose up -d
echo ">>> SYSTEM ONLINE: http://localhost:8069"
docker-compose logs -f web
