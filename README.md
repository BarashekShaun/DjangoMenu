#### Перед запуском необходимо выполнить следущие команды:
``` python
$ pip install --upgrade pip 
$ pip install -r requirements.txt
$ docker-compose up --build
```

#### Для запуска проекта в Debug-режиме:
``` python
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

#### Для создания суперпользователя:
``` python
$ python manage.py createsuperuser
```

#### В проекте использованы:
* PostgreSQL
* Django
* Docker

Версии можно посмотреть тут: [requirements.txt](jetbrains://pycharm/navigate/reference?project=UpTrader&path=menu_tree/requirements.txt)
