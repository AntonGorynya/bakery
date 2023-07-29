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

### Загрузка данных
Наполните базу начальными данными
```sh
python manage.py load https://raw.githubusercontent.com/Amartyanov1974/bakery-data/main/data_bakery.json
```

### Создание и мониторинг рекламных ссылок

Реализованы вде команды позволяющие создавать сокращенные ссылки при помощи API bitly, а также контролировать количество переходов по ним пользователей.

Необходимо в файл `.env` внести переменные:

`BITLY_ACCESS_TOKEN = 'Ваш токен'`,

он может быть получен после регистрации на сайте [bitly.com](https://bitly.com/).

`LINKS = '["Ваша ссылка", "Ваша ссылка"]'`.

Для создания реекламных ссылок и внесения их в базу данных, в командной строке необходимо ввести команду:
```sh
python manage.py create_bitlink
```
Для подсчёта количества переходов с внесением их в базу данных исользуется команда:
```sh
`python manage.py count_clicks`.
```