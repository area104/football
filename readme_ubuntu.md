cd /home
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

use admin
db.createUser({
  user: "admin1", 
  pwd: "qwerty",
  roles: [{ role: "readWrite", db: "footballdb" }]
})

use footballdb


sudo apt-get update && apt-get upgrade


sudo apt-get install ufw
sudo ufw default allow outgoing
sudo ufw default deny incoming
sudo ufw allow 80
sudo ufw allow 8000
sudo ufw allow 22
sudo ufw enable
sudo ufw status

sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi-py3


cd /etc/apache2/sites-available/ 
sudo cp 000-default.conf django_project.conf
sudo nano django_project.conf

============

Alias /static /home/footballresults_django/static_root
<Directory /home/footballresults_django/static_root>
    Require all granted
</Directory>
Alias /media /home/footballresults_django/media
        <Directory /home/footballresults_django/media>
                Require all granted
        </Directory>




<Directory /home/footballresults_django/footballresults_django>
            <Files wsgi.py>
        Require all granted
    </Files>
    </Directory>

WSGIScriptAlias / /home/footballresults_django/footballresults_django/wsgi.py
WSGIDaemonProcess django_app python-path=/home/footballresults_django python-home=/root/miniconda3/envs/ballres
WSGIProcessGroup django_app
===============


conda create --name ballres python=3.9
conda activate ballres 
conda update conda
conda update --all

sudo apt-get install apache2-dev

pip install -r requirements.txt
hostnamectl set-hostname django-server
nano /etc/hosts
45.150.129.100 django-server

cd /home/footballresults_django

python manage.py makemigrations footballresults
python manage.py makemigrations app_admins
python manage.py migrate

python manage.py runserver 0.0.0.0:8000

sudo chown -R 777  '/home/footballresults_django'
sudo chmod -R 777  '/home/footballresults_django'

sudo a2ensite django_project


sudo a2dissite 000-default.conf

cd /home

sudo chown :www-data footballresults_django/db.sqlite3
sudo chmod 777 footballresults_django/db.sqlite3
sudo chown 777 footballresults_django/db.sqlite3
sudo chown :www-data footballresults_django/
sudo chown -R :www-data footballresults_django/media
sudo chown -R 775 footballresults_django/media
cd /root/miniconda3/envs


sudo chown -R 777 'ballres'
sudo chmod -R 777 'ballres'

sudo ufw allow http/tcp
sudo service apache2 restart

sudo chmod -R 777 'envs'
sudo chown -R 777 'envs'
sudo chmod -R 777 'venv'
sudo chown -R 777 'venv'

sudo mv /root/miniconda3/envs/ballres /var/www/



sudo apt-get install python3-pip
sudo apt-get install python3-venv
sudo python3 -m venv venv
source ./venv/bin/activate

sudo chmod -R 777 'pythainlp-data'
sudo chown -R 777 'pythainlp-data'

db.runCommand({whatsmyuri: 1})