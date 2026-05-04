# Куда пойти — Москва глазами Артёма

Сайт с интерактивной картой Москвы и интересными местами. Авторский проект Артёма.


## Как запустить локально

### 1. Скачай репозиторий

```bash
git clone https://github.com/ВАШ_НИКНЕЙМ/where_to_go.git
cd where_to_go
```

### 2. Установи зависимости

```bash
pip install -r requirements.txt
```

### 3. Создай файл `.env` в корне проекта

Добавь туда следующие переменные окружения:

- SECRET_KEY=ваш-секретный-ключ
- DEBUG=True
- ALLOWED_HOSTS=127.0.0.1

### 4. Примени миграции

```bash
python manage.py migrate
```

### 5. Создай суперпользователя

```bash
python manage.py createsuperuser
```

### 6. Запусти сервер

```bash
python manage.py runserver
```

Сайт будет доступен по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000)

Админка: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## Загрузка тестовых данных

Чтобы загрузить место с фотографиями из JSON файла:

```bash
python manage.py load_place http://адрес/файла.json
```

Пример JSON файла с локацией:

```json
{
    "title": "Парк Горького",
    "imgs": [
        "https://example.com/img1.jpg"
    ],
    "description_short": "Главный парк Москвы",
    "description_long": "<p>Описание парка</p>",
    "coordinates": {
        "lat": 55.7300,
        "lng": 37.6011
    }
}
```

## Используемые технологии

- [Django](https://www.djangoproject.com/) — бэкенд
- [Leaflet](https://leafletjs.com/) — интерактивная карта
- [Vue.js](https://ru.vuejs.org/) — реактивные шаблоны
- [Bootstrap](https://getbootstrap.com/) — стили
- [TinyMCE](https://www.tiny.cloud/) — редактор текста в админке
- [django-admin-sortable2](https://django-admin-sortable2.readthedocs.io/) — сортировка фото в админке

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).
