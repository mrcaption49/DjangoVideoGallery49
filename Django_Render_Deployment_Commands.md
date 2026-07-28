# Django Deployment Commands (Render)

## 1. Install Required Packages

``` bash
pip install dj-database-url psycopg2-binary boto3 django-storages whitenoise gunicorn
```

Installs the packages required for PostgreSQL, AWS S3, static files, and
Gunicorn.

------------------------------------------------------------------------

## 2. Update `requirements.txt`

``` bash
pip freeze > requirements.txt
```

Saves all installed Python packages.

------------------------------------------------------------------------

## 3. Test Migrations Locally

``` bash
python manage.py makemigrations
python manage.py migrate
```

Creates and applies database migrations.

------------------------------------------------------------------------

## 4. Collect Static Files

``` bash
python manage.py collectstatic --noinput
```

Copies static files into the `staticfiles` directory for deployment.

------------------------------------------------------------------------

## 5. Run the Development Server

``` bash
python manage.py runserver
```

Starts the local Django development server.

------------------------------------------------------------------------

## 6. Commit Changes

``` bash
git add .
git commit -m "Prepare project for Render deployment"
git push origin main
```

Uploads the latest code to GitHub.

------------------------------------------------------------------------

## 7. Render Build Command

``` bash
pip install -r requirements.txt && python manage.py collectstatic --noinput
```

Installs dependencies and prepares static files during deployment.

------------------------------------------------------------------------

## 8. Render Start Command

``` bash
gunicorn videogallery.wsgi:application
```

Starts the Django application with Gunicorn.

------------------------------------------------------------------------

## 9. Run Database Migrations (Render Shell)

``` bash
python manage.py migrate
```

Creates all database tables in Render PostgreSQL.

------------------------------------------------------------------------

## 10. Create Admin User

``` bash
python manage.py createsuperuser
```

Creates an administrator account.

------------------------------------------------------------------------

## 11. Useful Management Commands

``` bash
python manage.py showmigrations
```

Shows migration status.

``` bash
python manage.py shell
```

Opens the Django interactive shell.

``` bash
python manage.py check
```

Checks the project for configuration issues.

------------------------------------------------------------------------

## Environment Variables (Render)

    DATABASE_URL=<Render PostgreSQL URL>
    SECRET_KEY=<Your Secret Key>
    DEBUG=False
    AWS_ACCESS_KEY_ID=<AWS Key>
    AWS_SECRET_ACCESS_KEY=<AWS Secret>
    AWS_STORAGE_BUCKET_NAME=photoalbum49
    ALLOWED_HOSTS=.onrender.com

These values are configured in the Render dashboard and should not be
hardcoded in your project.
