
 # Описание проекта
    Проект **YaMDb** собирает отзывы пользователей на различные произведения.

    # Алгоритм регистрации пользователей
    1. Пользователь отправляет POST-запрос на добавление нового пользователя с параметрами `email` и `username` на эндпоинт `/api/v1/auth/signup/`.
    2. **YaMDB** отправляет письмо с кодом подтверждения (`confirmation_code`) на адрес  `email`.
    3. Пользователь отправляет POST-запрос с параметрами `username` и `confirmation_code` на эндпоинт `/api/v1/auth/token/`, в ответе на запрос ему приходит `token` (JWT-токен).
    4. При желании пользователь отправляет PATCH-запрос на эндпоинт `/api/v1/users/me/` и заполняет поля в своём профайле (описание полей — в документации).

    # Пользовательские роли
    - **Аноним** — может просматривать описания произведений, читать отзывы и комментарии.
    - **Аутентифицированный пользователь** (`user`) — может, как и **Аноним**, читать всё, дополнительно он может публиковать отзывы и ставить оценку произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы; может редактировать и удалять **свои** отзывы и комментарии. Эта роль присваивается по умолчанию каждому новому пользователю.
    - **Модератор** (`moderator`) — те же права, что и у **Аутентифицированного пользователя** плюс право удалять **любые** отзывы и комментарии.
    - **Администратор** (`admin`) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям. 
    - **Суперюзер Django** — обладет правами администратора (`admin`)
## Название проекта: 
**YaMDb**

## Функциональность:
- Создание, чтение, обновление и удаление отзывов
- Создание, чтение, обновление и удаление комментариев
- Валидация данных при создании отзывов и комментариев
- Аутентификация с использованием JWT-токенов

## Стек технологий:
- Язык программирования: Python
- Фреймворк: Django REST framework
- База данных: SQLite
- Аутентификация: JWT-токены

## Развёртывание проекта:
1. Склонировать репозиторий на локальную машину
2. Установить зависимости из requirements.txt
3. Запустить сервер командой python manage.py runserver
4. Загрузить данные командой python manage.py loaddata

## Примеры запросов и ответов:
### Создание отзыва:
**Request:**
POST /api/reviews/
{
  "text": "Отличный продукт!",
  "author": "user123",
  "score": 9,
  "pub_date": "2022-10-15T10:00:00Z"
}

**Response:**
201 Created
{
  "id": 1,
  "text": "Отличный продукт!",
  "author": "user123",
  "score": 9,
  "pub_date": "2022-10-15T10:00:00Z"
}


### Получение всех комментариев:
**Request:**
GET /api/comments/

**Response:**
200 OK
[
  {
    "id": 1,
    "text": "Согласен с автором!",
    "author": "user456",
    "pub_date": "2022-10-16T12:00:00Z"
  },
  {
    "id": 2,
    "text": "Спасибо за информацию!",
    "author": "user789",
    "pub_date": "2022-10-16T13:00:00Z"
  }
]


## Автор:
Автор проекта - [Sherdiyor]

