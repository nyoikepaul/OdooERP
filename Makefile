.PHONY: up down restart logs shell reset

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f web

shell:
	docker compose exec web /bin/bash

reset:
	docker compose down -v
	docker compose up -d
	@echo "System reset. Odoo is re-initializing the database..."

prod-up:
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d

prod-down:
docker compose -f docker-compose.yml -f docker-compose.prod.yml down

prod-logs:
docker compose -f docker-compose.yml -f docker-compose.prod.yml logs -f web

backup:
docker compose exec db pg_dump -U odoo odoo > backup_$(shell date +%Y%m%d_%H%M%S).sql
@echo "Backup created"
