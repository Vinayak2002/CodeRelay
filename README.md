<h1 align =center>Hostel Management WebApp </h1>
<p align =center>CodeRelay AMV</p>
<p align="center">
  <img width="300" src="https://github.com/Vinayak2002/CodeRelay/blob/main2/static/Resources/Hostel-removebg.png" alt="Material Bread logo">
</p>


This webapp can be used for hostel complaint management services. There are two groups of users:
students - hostel dwellers
officers - managers - people who are supposed to resolving the complaints

# Features - 

* Registration - Users can register in this webapp.
* Complaints Logging - Complaints can be posted only by students.
* Complaints Management - Officers can handle complaints.


# Technologies used:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) <br />
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) <br />
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) <br />
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) <br />
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white) <br />
![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white) <br />
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) <br />
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white) <br />
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) <br />

# Steps to setup on your own local machine:
* Pull the code from github.
* Create a virtual environment and install django crispy-bootstrap5 and psycopg2-binary python modules.
```
pip install django crispy-bootstrap5 psycopg2-binary
```
* Get database credentials of a postgres database using heroku for free.
* Add the following lines in the settings.py file.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database-name',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'host-address',
        'PORT': 'port'
    }
}
```
* Migrate the database
```
python manage.py makemigrations

python manage.py migrate
```
* Run the server
```
python manage.py runserver
```
* Now the server will be running and you can use the webapp.
