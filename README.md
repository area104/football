# footballresults_django
football results using django
python manage.py startapp app_admins  


cd C:\Users\wanch\OneDrive\เอกสาร\GitHub\footballresults_django
pip install django
django-admin startproject footballresults_django
cd footballresults_django

python manage.py startapp footballresults
pip install pymongo

mongodb://localhost:27017


conda activate ballres
pip freeze > requirements.txt


/var/www/footballresults_django/venv_ballres
use footballdb3
db.createCollection("football_league")

python manage.py makemigrations
python manage.py migrate
python manage.py runserver


mongosh
use footballdb

db.db_admin_settings.insertOne({
  "id": 41,
  "web_api": "https://api.football-data-api.com/",
  "api_key": "ccbef",
  "date_update": 0,
  "line_api": "Scj7c",
  "userid": 1,
  "time_league_update": 1000,
  "time_time_update": 100,
  "time_matches_update": 1,
  "league_list": "England - Championship\r\nEngland - Premier League\r\nEngland - FA Cup",
  "user_get_api": 0
})



conda activate ballres
python manage.py makemigrations footballresults
python manage.py makemigrations app_admins
python manage.py migrate
python manage.py runserver

England - Championship
England - Premier League
England - FA Cup
