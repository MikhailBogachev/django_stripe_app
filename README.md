# Django app + Stripe
### Описание
Проект в рамках тестового задания
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/MikhailBogachev/django_stripe_app.git
```

```
cd django_stripe_app
```

### Запуск с помощью Docker:
Создать файл .env с переменными окружения (пза основу можно взять файл env_example):
```
STRIPE_PUBLISHABLE_KEY=
STRIPE_SECRET_KEY=
SECRET_KEY=
DEBUG=
```
STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY - API ключи для работы со Stripe. Брать тут https://dashboard.stripe.com/test/apikeys
SECRET_KEY - секретный ключ Django. Необязательный.  
DEBUG - режим дебага True/False. Необязательный. по дефолту True.  

Создать образ:

```
docker compose build
```

Создать и запустить контейнер:

```
docker compose up -d
```

Заполнить БД тестовыми данными:

```
docker exec -it django_stripe_app-web-1 python manage.py loaddata items.json
```

После этого будут доступны страницы с объектами: http://localhost:8000/item/{id},
  id - уникальный идентификатор объекта. После загрузки тестовых данных на предыдущем шаге доступны объекты с id от 1 до 5 включительно.

Для доступа к админ панели (http://localhost:8000/admin/) необходимо создать суперпользователя:

```
docker exec -it django_stripe_app-web-1 python manage.py createsuperuser
```
