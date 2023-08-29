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

pip freeze > requirements.txt 
pip install djongo pymongo pytz


conda activate ballres
python manage.py makemigrations footballresults
python manage.py makemigrations app_admins
python manage.py migrate


python manage.py runserver

===================================

# Install Miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
source ~/.bashrc
conda --v
pip -V
pip3 -V


sudo apt update
sudo apt install mongodb
sudo systemctl start mongodb
sudo systemctl enable mongodb
sudo systemctl status mongodb
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu $(lsb_release -cs)/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list

sudo apt update
sudo apt install -y mongodb-mongosh

mongosh
==============================

conda activate ballres
pip freeze > requirements.txt

https://drive.google.com/drive/folders/1absiNmWlXzMpvKdXfetzuBwd2D9S6X_W?usp=drive_link


conda create --name ballres python=3.9
conda activate ballres 
conda update conda
conda update --all


pip install -r requirements.txt

mongosh
use admin
db.createUser({
  user: "admin1", 
  pwd: "qwerty",
  roles: [{ role: "readWrite", db: "footballdb" }]
})

use footballdb3
db.createCollection("football_league")

python manage.py makemigrations
python manage.py migrate
python manage.py runserver


mongosh
use footballdb3

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

db.db_admin_settings.find()


sudo lsof -iTCP -sTCP:LISTEN | grep mongo

python manage.py runserver 0.0.0.0:8000
hostname -I


====================================


cd Documents
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

bash Miniconda3-latest-Linux-x86_64.sh
source ~/.bashrc
conda --v
pip -V
pip3 -V

sudo apt update

conda create --name ballres python=3.9
conda activate ballres 
conda update conda
conda update --all
pip install -r requirements.txt



sudo apt update



sudo apt install mongodb
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu $(lsb_release -cs)/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list


sudo systemctl start mongodb
sudo systemctl enable mongodb
sudo systemctl status mongodb



sudo apt update
sudo apt install -y mongodb-mongosh

mongosh

use admin
db.createUser({
  user: "admin1", 
  pwd: "qwerty",
  roles: [{ role: "readWrite", db: "footballdb" }]
})
db.runCommand({ whatsmyuri: 1 })

use footballdb
db.createCollection("football_league")

sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi-py3

cd /etc/apache2/sites-available/ 


ps aux | grep -i apt
ps aux | grep -i dpkg
sudo rm /var/lib/dpkg/lock-frontend
sudo rm /var/lib/dpkg/lock


sudo apt-get install ufw
sudo ufw default allow outgoing
sudo ufw default deny incoming

sudo ufw allow 8000
sudo ufw allow 22
sudo ufw enable
sudo ufw status

sudo chown -R 777 '/home/nick4/miniconda3/envs/ballres'
sudo chmod -R 777 '/home/nick4/miniconda3/envs/ballres'

conda activate ballres
python manage.py makemigrations footballresults
python manage.py makemigrations app_admins
python manage.py migrate
python manage.py runserver
python manage.py collectstatic
sudo mv footballresults_django /var/www
sudo chown -R 777  'footballresults_django'
sudo chmod -R 777  'footballresults_django'
python manage.py runserver 0.0.0.0:8000
cd /etc/apache2/sites-available/ 
ls
sudo cp 000-default.conf django_project.conf

/home/nick4/miniconda3/envs/ballres
sudo nano /etc/apache2/sites-available/django_project.conf
===========================================

Alias /static /var/www/footballresults_django/static_root
<Directory /var/www/footballresults_django/static_root>
    Require all granted
</Directory>
Alias /media /var/www/footballresults_django/media
        <Directory /var/www/footballresults_django/media>
                Require all granted
        </Directory>




<Directory /var/www/footballresults_django/footballresults_django>
            <Files wsgi.py>
        Require all granted
    </Files>
    </Directory>

WSGIScriptAlias / /var/www/footballresults_django/footballresults_django/wsgi.py
WSGIDaemonProcess django_app python-path=/var/www/footballresults_django python-home=/home/nick4/miniconda3/envs/ballres
WSGIProcessGroup django_app

===========================================

sudo a2ensite django_project.conf
sudo a2dissite 000-default.conf
sudo systemctl reload apache2
cd /var/www


sudo chown :www-data footballresults_django/db.sqlite3
sudo chmod 664 footballresults_django/db.sqlite3
sudo chown :www-data footballresults_django/

sudo chown  :www-data footballresults_django/media
sudo chown -R 775 footballresults_django/media

sudo ufw allow 80
sudo ufw delete allow 8000
sudo ufw allow http/tcp
sudo service apache2 restart

sudo apt  install curl
curl ifconfig.me
sudo systemctl reload apache2
===========================================












sudo tail -f /var/log/apache2/error.log
        
        https://drive.google.com/drive/folders/1absiNmWlXzMpvKdXfetzuBwd2D9S6X_W?usp=drive_link

https://docs.google.com/document/d/1L6ALpby7SJAM1xpNWYKeuz3VfCw7SSYnTSse6UsU704/edit?fbclid=IwAR3KyzK1TGolEAIyN4Uk7wbfWlVGpkoIq4DZFIZD60rzJJp6PLh8Y_-NUfo


# Download the tarball
wget https://downloads.mongodb.com/compass/mongosh-1.0.3-linux.tgz

# Extract the tarball
tar -xvzf mongosh-1.0.3-linux.tgz

# Navigate to the extracted directory
cd mongosh-1.0.3-linux

# Run mongosh
./mongosh



pip install Django
# pip install mkl-fft
pip install numpy
pip install pandas
# pip install PyJWT
pip install pymongo
pip install pytz
pip install requests





import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']
collection = db['your_collection_name']

print(db.list_collection_names())  # Print list of collection names


pip install --upgrade django djongo pymongo

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'footballdb',
        'ENFORCE_SCHEMA': True,
        'CLIENT': {
            'host': 'localhost',       # Change 'your_host' to 'localhost'
            'port': 27017,             # Change 'your_port' to 27017
            'username': 'admin1',      # Leave 'your_username' empty if no username required
            'password': 'qwerty',      # Leave 'your_password' empty if no password required
            'authSource': 'admin',
            'authMechanism': 'SCRAM-SHA-1',
        }
    }
}

