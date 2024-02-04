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

Версии можно посмотреть тут: [requirements.txt](https://github.com/BarashekShaun/DjangoMenu/blob/262965ca4ba21f1bac76d66c5b7f7fe09b0d9692/menu_tree/requirements.txt)
