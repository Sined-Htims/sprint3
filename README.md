# Проект Blogicum

## Цель работы:

Научится выполнять следующее:  
1. Создавать модели БД(*models.py*) и логику взаимодействия с данными из БД(*views.py*). :heavy_check_mark:
2. Настраивать админ-зону проекта. :heavy_check_mark:
3. Подключать готовые шаблоны страниц к проекту. :heavy_check_mark:

## Разворачивание проекта.

1. Установить виртуальное окружение.

```bash
python -m venv venv
```

2. Активировать виртуальное окружение.

```bash
. venv/Scripts/activate
```

3. Установить зависиости из requirements.txt.

```bash
pip install -r requirements.txt
```

4. Перейти в директорию с файлом "manage.py".

```bash
cd ./<название_директории>/
```

5. Применить миграции.

```bash
python manage.py migrate
```

6. Создать суперпользователя.

```bash
python manage.py createsuperuser
```

7. Запустить сервер.

```bash
python manage.py runserver
```

8. Наслаждаться :coffee:  

**Приведенные команды используются для Bash/OC Windows*  
**Это второй спринт из курса "Бэкенд на Django Ver.2.0" от Яндекс.Практикум*
