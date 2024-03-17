1. main.py - основной файл приложения
2. models.py - файл для определения моделей данных
3. database.py - файл для настройки подключения к базе данных
4. alembic - директория для хранения миграций Alembic
5. requirements - необходимые библиотеки

Для миграций к БД PostgreSQL:
alembic init alembic - иницилизация
alembic revision --autogenerate -m "create sessions table" - создание миграции
Миграция будет находиться в директории alembic/versions
alembic upgrade head - применение миграции к бд

Нужно будет изменить "SQLALCHEMY_DATABASE_URL" в файле database.py на вашу БД.
Также нужно изменить "sqlalchemy.url = driver://user:pass@localhost/dbname" в файле alembic.ini на вашу БД.

Запуск программы:
uvicorn main:app --reload
