# Задача 1:
Необходимо разработать API сервис, который предоставит возможность пользователям зарегистрироваться(логин/пароль/имя), авторизоваться(логин пароль) и подключать телеграм бота к своему аккаунту. БД PostgreSQL.
# Задача 2:
(не в FastApi, а отдельно) Бот(данные из # задачи 1 PostgreSQL) должен отвечать на любое отправленное ему сообщение, сообщая количество символов в этом сообщении. При отправке сообщения боту, он вернет ответ вида "Вы отправили сообщение длиной Х символов.", где Х - количество символов в сообщении.
Требования к выполнению задач:
Использование Docker для контейнеризации приложения.
Использование PostgreSQL для хранения пользовательских данных.
Использование FastAPI для создания и реализации API.
Использование Aiogram для работы с Telegram API.
Использование Pydantic для валидации данных.

Дополнительные требования:
Разместить код на GitHub.
Предоставить Docker файл для сборки контейнера.
Написать грамотную инструкцию по развертыванию сервиса.