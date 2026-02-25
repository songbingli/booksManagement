# AGENTS.md

## Cursor Cloud specific instructions

### Overview

This is a **Django book management system** (图书管理系统) with a user-facing frontend and a Django admin backend (enhanced with `simpleui`).

- Frontend: `http://localhost:8000/`
- Admin backend: `http://localhost:8000/admin/`

### Compatibility notes

- The codebase was originally written for Django 2.2, but requires **Django 3.2 LTS** to work with Python 3.12 and pymysql 1.0+. The `{% load staticfiles %}` template tag was updated to `{% load static %}` for Django 3.x compatibility.
- The original migration files were broken (referenced wrong model fields). They have been regenerated from the current `models.py`.

### Starting services

1. **MySQL**: `sudo mysqld --user=mysql --datadir=/var/lib/mysql &` then `sudo chmod 755 /var/run/mysqld`
2. **Django dev server**: `python3 manage.py runserver 0.0.0.0:8000` (from `/workspace`)

### Database

- MySQL database name: `books`, user: `root`, password: `root`, host: `localhost`, port: `3306`
- To reset: `sudo mysql -u root -proot -e "DROP DATABASE IF EXISTS books; CREATE DATABASE books DEFAULT CHARACTER SET utf8mb4;"` then `python3 manage.py migrate`
- Admin superuser: create with `DJANGO_SUPERUSER_PASSWORD=admin123 python3 manage.py createsuperuser --username admin --email admin@example.com --noinput`

### Gotchas

- The CAPTCHA font file at `static/STXIHEI.TTF` is a copy of `wqy-microhei.ttc` from the system fonts. If missing, the login CAPTCHA will 500.
- `ALLOWED_HOSTS` in `settings.py` is set to `['*']` for development. Keep this in dev mode.
- There are no automated tests in this codebase. Manual testing via the browser is the primary testing method.
- No linter configuration exists. Use `python3 manage.py check` for Django system checks.
