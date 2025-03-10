Сервис рассылки уведомлений пользователям
=====

Описание проекта
----------
Проект представляет собой сервис для работы с данными клиентов и управления рассылками сообщений.

Проект разворачивается в пяти Docker контейнерах: web-приложение для админки и api, celery-приложение для рассылки, postgresql-база данных, redis-база данных, и nginx-сервер.

Настроены модели для отображения в панели администратора.

Системные требования
----------

* Python 3.8+
* Docker
* Works on Linux

Стек технологий
----------

* Python 3.8+
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
git clone git@github.com:NikitaChalykh/backend.git

cd backend # Переходим в директорию с проектом
```

2. Создайте файл ```.env``` используя ```env.example``` в качестве шаблона в папке infra

3. Установка и запуск сервиса в контейнере:
```bash 
docker-compose up -d
```

4. Запуск миграций, сбор статики и создание суперпользователя:
```bash 
docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py collectstatic --no-input

docker-compose exec web python manage.py
```

Работа с проектом
----------
Документация по работе API сервиса:

```http://127.0.0.1/redoc/```

```http://127.0.0.1/swagger/```

Админка сервиса:

```http://127.0.0.1/admin/```
