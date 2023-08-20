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

use admin
db.createUser({
  user: "", 
  pwd: "",
  roles: [{ role: "readWrite", db: "footballdb" }]
})


pip install djongo pymongo pytz

python manage.py makemigrations footballresults
python manage.py makemigrations
python manage.py migrate

conda activate ballres
python manage.py runserver