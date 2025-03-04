API для системы сервиса рассылок уведомлений
=====

Описание проекта
----------
Проект состоит из проектируемого API сервиса для работы с данными клиентов и управления рассылками сообщений.

API сервис реализуется на базе фреймворка DRF.

Системные требования
----------

* Python 3.8+
* Docker
* Works on Linux

Стек технологий
----------

* Python 3.8
* Django 3.1
* Django Rest Framework
* PostreSQL
* Nginx
* gunicorn
* Docker, Docker Compose
* Сelery
* Redis

Установка проекта из репозитория
----------
1. Клонирование репозитория:
```bash 
git clone git@github.com:NikitaChalykh/mailing_service.git

cd mailing_service # Переходим в директорию с проектом
```

2. Создайте файл .env используя .env.example в качестве шаблона в папке infra

3. Установка и запуск сервиса в контейнере:
```bash 
docker-compose up -d
```

4. Запуск миграций и сбор статики:
```bash 
docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py collectstatic --no-input 
```

Документация к проекту
----------
Документация для API сервиса после установки: 

```http://127.0.0.1/redoc/```

```http://127.0.0.1/swagger/```
