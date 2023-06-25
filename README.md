# pet_landing

<img width="1024" alt="Screenshot 2023-06-25 at 15 27 21" src="https://github.com/igor-gorovenko/pet_landing/assets/59226858/aabd5d98-b510-4e0d-87f5-74b9e4bc1090">

Превью проекта

## Инструкция по установке и запуску проекта

Скопируйте репозиторий
```
git clone git@github.com:igor-gorovenko/pet_landing.git
```

У вас должен быть установлен питон 3 версии, скачать можно тут: https://www.python.org/

Создаем виртуальное окружение:
```
python3 -m venv .venv
```

Активируем виртуальное окружение:

```
source .venv/bin/activate
```

Далее устанавливаем все из файла requirements.txt, для этого можно использовать команду:

```
python -m pip install <name_packages>
```

Теперь нужно зайти в папку где лежит manage.py
```
cd landing_project
```

Делаем миграции
```
python manage.py migrate
```

Что бы запустить сервер, для этого нужно перейти в папку с файлом manage.py и ввести команду:
```
python manage.py runserver
```
