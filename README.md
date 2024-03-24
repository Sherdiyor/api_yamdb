### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone ...
```

```
cd ...
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Загрузить данные в БД из CSV:

```
python3 manage.py load_data
```

Запустить проект:

```
python3 manage.py runserver
```
