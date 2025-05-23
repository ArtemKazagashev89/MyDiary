# MyDiary

MyDiary — это веб-приложение для ведения личного дневника, разработанное с использованием Django и PostgreSQL. Оно позволяет пользователям регистрироваться, аутентифицироваться и управлять своими записями.

## Установка и запуск

### Требования

- Python 3.11 и выше
- Docker и Docker Compose
- PostgreSQL

### Клонирование репозитория
bash
git clone https://github.com/ArtemKazagashev89/MyDiary.git
cd MyDiary

### Настройка окружения

1. Создайте файл `.env` в корне проекта и добавьте необходимые переменные окружения:
SECRETKEY=your-secret-key
DATABASEURL=postgres://user:password@db:5432/dbname
2. 2. Убедитесь, что файл `requirements.txt` содержит все необходимые зависимости.

### Запуск приложения

1. Соберите и запустите контейнеры:
bash
docker-compose up --build
2. 2. Дождитесь, пока все контейнеры запустятся. Приложение будет доступно по адресу `http://localhost:8000`.

### Миграция базы данных

После первого запуска выполните миграции:
bash
docker-compose exec web python manage.py migrate

### Статические файлы

Для сбора статических файлов выполните:
bash
docker-compose exec web python manage.py collectstatic --noinput

### Использование

- **Регистрация:** Пользователи могут создать новый аккаунт.
- **Вход:** Пользователи могут входить в систему с использованием своей электронной почты и пароля.
- **Управление записями:** Пользователи могут добавлять, редактировать и удалять записи в своем дневнике.

## Тестирование

Для запуска тестов выполните:
bash
docker-compose exec web python manage.py test

## Контакт для связи с командой разработки:
`tema124ru@mail.ru`


## Источники
Программа создана при поддержке онлайн-школы [skypro@skyeng.ru](https://sky.pro/#giftpopup) 

 ![alt текст](https://static.tildacdn.com/tild3364-3965-4237-b664-363533643431/Group_1321317003.svg)

