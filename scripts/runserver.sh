#!/usr/bin/env bash
if [ -f .env ]; then
    . ./.env
fi

. ./scripts/migrations.sh
. ./scripts/create_superuser.sh
python ./manage.py runserver
