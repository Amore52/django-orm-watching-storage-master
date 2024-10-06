# Пульт охраны банка.

Это внутренний репозиторий для сотрудников банка "Сияние". Если вы попали в этот репозиторий случайно
то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать
код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны - это сайт, который можно подключить к удаленной базе данных с визитами и карточками пропуска 
сотрудников нашего банка.

### Как установить.

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:<br>
**pip install -r requirements.txt**

Для запуска в терминале ввести:<br>
**python manage.py runserver 0.0.0.0:8000**
В адресной строке браузера ввести - http://127.0.0.1:8000/


В коде присутствуют следующие переменные окружения: 
DATABASE_HOST - хост, на котором развернута база данных.<br>
DATABASE_PORT - порт, на котором база данных принимает подключения.<br>
DATABASE_NAME - имя базы данных, к которой будет происходить подключение.<br>
DATABASE_USER - имя пользователя, который будет использоваться для подключения к базе данных.<br>
DATABASE_PASSWORD - пароль, связанный с именем пользователя для подключения к базе.<br>
SECRET_KEY - ваш секретный ключ.

Цель проекта:
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.

