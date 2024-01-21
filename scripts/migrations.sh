#!/usr/bin/env bash
if [ -f .env ]; then
    . ./.env
fi

echo 'Making migrations'
python ./manage.py makemigrations --noinput || exit 1
echo 'Migrating'
python ./manage.py migrate --noinput || exit 1
