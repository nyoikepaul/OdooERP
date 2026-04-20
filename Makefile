.PHONY: up down restart logs shell reset

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f web

shell:
	docker-compose exec web /bin/bash

reset:
	docker-compose down -v
	docker-compose up -d
	@echo "System reset. Odoo is re-initializing the database..."
