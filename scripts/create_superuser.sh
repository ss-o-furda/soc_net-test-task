#!/usr/bin/env bash
if [ -f .env ]; then
    . ./.env
fi

echo 'Creating user admin'
echo "from django.contrib.auth.models import User; User.objects.filter(email='${SUPERUSER_EMAIL}').delete(); User.objects.create_superuser('${SUPERUSER_USERNAME}', '${SUPERUSER_EMAIL}', '${SUPERUSER_PASSWORD}')" | python ./manage.py shell
