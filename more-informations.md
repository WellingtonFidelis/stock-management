# More informations about the project

## First commands

1. python -m venv ./venv
2. source venv/bin/activate
3. pip install --upgrade pip
4. pip install django
5. django-admin startproject core .
6. python manage.py makemigrations
7. python manage.py migrate
8. python manage.py createsuperuser

## Super user

- login: admin
- password: admin

## Creating the apps

1. python manage.py startapp stock_management
2. python manage.py makemigrations
3. python manage.py migrate
