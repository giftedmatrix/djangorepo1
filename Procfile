web: gunicorn project.wsgi:application --log-file - --log-level debug
python manage.py collecstatic --noinput
release: python manage.py makemigrations
release: python manage.py migrate
