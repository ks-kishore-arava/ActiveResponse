#!/bin/bash
set -e

# Create database and user
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE postgres;
    CREATE USER "$POSTGRES_USER" WITH PASSWORD "$POSTGRES_PASSWORD";
    GRANT ALL PRIVILEGES ON DATABASE postgres TO "$POSTGRES_USER";
EOSQL