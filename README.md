# Simcard_CRUD_System
Realization Simcard CRUD Management System built with Django

SimcardCRUD - папка Django-проекта, реализующего CRUD-систему 

SimcardCRUD is the folder of the Django project implementing the CRUD system 

Simcard CRUD-System Видеодемонстрация: https://youtu.be/mBsRfhctuZU

Simcard CRUD-System Video Demonstration: https://youtu.be/mBsRfhctuZU

SQL Queries - папка с SQL запросами к базе данных (не та что использовалась в CRUD-системе)

SQL Queries is a folder with SQL queries to the database (not the one used in the CRUD system)


# Starting project 

First time: `docker compose up -d --build`

Casually: `docker compose up -d`

If changes to `Dockerfile` and/or `docker-compose.yml` were applied: `docker compose up -d --build`

# .env configuration

Rename `.env.example` file into `.env`

Enter `yandex email address` that is gonna be used

Create `yandex app password` and enter it 

# Pytest startup

__All tests are running in docker__

All tests: `docker compose exec webapp pytest` or `docker compose exec webapp pytest -v`

Specific file: `docker compose exec webapp pytest CRUD_System/tests/views_tests.py`

Specific test in file: `docker compose exec webapp pytest CRUD_System/tests/views_tests.py::test_authenticated_main_page`

