# Онлайн-энциклопедия на Django

## Установка
```bash
git clone <ссылка на репозиторий>
cd myproject
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
