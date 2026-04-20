#!/usr/bin/env bash
# wait-for-db.sh: Expert-level service synchronization

# Load your core utils for that clean logging
# Assuming bash-utils is a sibling or sub-repo
source "../bash-utils/lib/core.sh" 2>/dev/null || echo "Core lib not found, using raw echo"

log_info "Waiting for Postgres to be ready on $DB_HOST:$DB_PORT..."

until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$POSTGRES_USER"; do
  log_warn "Postgres is unavailable - sleeping..."
  sleep 2
done

log_succ "Postgres is up! Initializing Odoo..."
exec "$@"
