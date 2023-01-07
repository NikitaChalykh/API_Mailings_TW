REST API for notification mailing service system
=====

Functional requirements
----------
[Link to Terms of Reference](https://www.craft.do/s/n6OVYFVUpq0o6L)

Project Description
----------
The project consists of a projected API service for working with customer data and managing message distributions.

The API service is implemented on the basis of the DRF framework.

System requirements
----------

* Python 3.6+
* Docker
* Works on Linux, Windows, macOS, BS

Technology stack
----------

* Python 3.8
* Django 3.1
* Django Rest Framework
* PostReSQL
* nginx
* gunicorn
* Docker
* Cellery
* Redis

Installing a project from a repository (Linux and macOS)
----------
1. Clone the repository and go to it on the command line:
```bash
git clone git@github.com:NikitaChalykh/API_Mailings_TW.git

cd API_Mailings_TW
```

2. Create and open the ```.env``` file with environment variables:
```bash
cd infra

touch .env
```

3. Fill in the ```.env``` file with environment variables as follows:
```bash
echo DB_ENGINE=django.db.backends.postgresql >> .env

echo DB_NAME=postgres >> .env

echo POSTGRES_PASSWORD=postgres >> .env

echo POSTGRES_USER=postgres >> .env

echo DB_HOST=db >> .env

echo DB_PORT=5432 >> .env

echo BROKER=redis://redis >> .env

echo BROKER_URL=redis://redis:6379/0 >> .env
```
Token for the service of sending messages according to the terms of reference
```bash
echo SENDING_API_TOKEN=****************** >> .env
```

4. Installing and running the application in containers:
```bash
docker-compose up -d
```

5. Run migrations and collect statics:
```bash
docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py collectstatic --no-input
```
Project Documentation
----------
Documentation for the API after installation is available at:

```http://127.0.0.1/redoc/```

```http://127.0.0.1/swagger/```
