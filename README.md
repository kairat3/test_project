Приветствую!

Я долго пытался поднять проект с html, bootstrap но к сожалению больше
одной или двух страничек поднять не получалось так как переставали работать эндпоинты:(
поэтому поднял базу данных с нужными эндпоинтами. Проверки все делались с Postman
Реализован JWT токен с активацией через почту
после активации, логинимся и получаем access токен
и введя его в headers следующим образом проверяем наши эндпоинты, кидаем запросы delete, update, create итд: 

key: Authorization Value: Token <сам токен>

Все установленные библиотеки были описаны в requirements.txt
Опишу инструкцию по запуску проекта на вашей локалке:
Открываем новый проект с пайчарма
В терминале вводим следующую команду:

git clone https://github.com/kairat3/test_project.git

после того как проект загрузился, вводим следующую команду:
pip install -r requirements.txt
(Это должно происходить в виртуальном окружении)
была использована база данных postgresql, и настройки указаны в корневом файле .env
поэтому рекомендую вам изменить настройки:
DB_NAME=
DB_USER=
DB_PASSWORD=
либо переключить в settings.py на sqllite
*** В файле .env находятся данные почты с которой отправляется письмо на почту для регистрации

После того как мы разобрались с бд, вводим в терминале следующее:
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser   "советую создавать админа с окончанием @gmail.com так как у нас customuser"

