# CourseGPT

## Install
```shell
python -m virtualenv .venv
. .venv/bin/activate
pip install -r requirements.txt
```
## Create env file
simply copy the `.env-example` to a new file named `.env`.
Then you can set your configs in this new `.env` file.

## Connect to Postgres
First create a database named `course_gpt` in postgres by:
```shell
    sudo -i -u postgres psql
    CREATE DATABASE course_gpt;
```
Then set the DATABASE_URL in the `.env` file like this example:
```text
DATABASE_URL=postgres://<USERNAME>:<PASSWORD>@127.0.0.1:5432/course_gpt
```

## Migration
```shell
python manage.py migrate
```

## Run
```shell
python manage.py runserver
```

## Admin panel
You can enter the admin panel (http://127.0.0.1:8000/admin) with the username `admin` and the password `admin`.