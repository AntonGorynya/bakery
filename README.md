# bakery

### Как установить
Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Установите зависимости:

```sh
pip install -r requirements.txt
```
Перед установкой создайте файл **.env** в папке **where_to_go** вида:
```properties
SECRET_KEY='ваш ключ'
DEBUG=False
ALLOWED_HOSTS=.example.com,127.0.0.1
```
Вы можете сгенерировать ключ командой
```sh
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Создайте базу данных SQLite

```sh
python manage.py migrate
```
Создайте суперпользователя
```sh
python manage.py createsuperuser
```