# python-django-restapi-docker-demo

Sample project to demo the usage of Restful webservices with Django and Mysql.


1. Go to https://www.python.org/downloads/ 
Select latest python version and download
Install the installer file in windows
2. In CMD , Check python --version or python -V
and Python3 comes with in-built pip installation.
Check -> pip --version or pip3 -V
3. Installing Django -> pip3 install django
check django version -> django-admin --version
4. Go to any folder where you want to create project and then Create Project  using command -> django-admin startproject myDjangoApp
Inside your project , there will be python file manager -> manage.py file
Run this command to start your development server-> python manage.py runserver
5. application will start , open browser of any wish and run localhost:8000/
6. install DjangoRestFramework using command -> pip install djangorestframework
after successfull installation , run in terminal =>  pip show djangorestframework ., you ll get below output
Name: djangorestframework
Version: 3.15.1
7. create new app using -> python manage.py startapp BooksInfo

8. Go to settings.py in main myDjangoApp settings.py and add rest_framework and app name in INSTALLED_APPS
i.e , 'rest_framework'
	  'BooksInfo'

When ever you run startapp appName -> it will create app with following files

BooksInfo
	>Migrations
		- init.py
	-init.py
	-admin.py
	-apps.py
	-models.py
	-tests.py
	-views.py


DjangoRestApiExample
	BooksInfo
		migrations
			__init__.py
		__init__.py
		admin.py
		apps.py
		models.py
		tests.py
		views.py
	DjangoRestApiExample
		__init__.py
		asgi.py
		settings.py
		urls.py
		wsgi.py
db.sqlite3
manage.py

8. run application using python manage.py runserver
9. create models, serializers , view and urls (already created in repo)
10. Then run  -> python manage.py makemigrations (this will create migrations inside /migrations folder)
		     -> python manage.py migrate (this will migrate , migrations scripts to default database (db.sqlite3) ) 
		  
11. Connecting with Mysql database instead of default db.sqlite3 database :

in requirements.txt file , add mysqlclient and then run => pip install -r requirements.txt
then check mysqlclient version => pip show mysqlclient

Notice this info in terminal:
---------
Name: mysqlclient
Version: 2.2.4
Summary: Python interface to MySQL

in main app settings.py , comment default databases ., 

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
     }
 }
 
and add your database like below

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

now run python application  using => python manage.py runserver
=> make sure tables created in  mysql, if any table not created ,then run syncdb like below.,
python manage.py migrate --run-syncdb 

12. start your app using python manage.py runserver, Test the api's GET, POST , PUT , DELETE ,OPTIONS , HEAD etc.

Docker:
-------
1. Make sure you have docker /docker compose /docker desktop installed in your machine.
2. Run docker --version , you should get output like below..
		Docker version 20.10.14, build a224086
3. create file name Dockerfile (f should be small in Dockerfile) in project/app root folder.(already created in repo)
4. open cmd in project path (ex: c/users/docs/project/django-test-application/) in my case.
5. run docker build -t django-restapi-example .    [make sure (.) is mandatory, it means all the files to build present in project]
6. run docker images , your images should be created with name django-restapi-example
7. Stop your application in local IDE , if already running..
8. Start you docker container using command in terminal in project path ->  docker run --name my-app -p8000:8000 django-restapi-example
9. Post successful completion of container up , run localhost:8000/ in browser.You ll get results from container.

if you want to remove container,images , run below commands,

10. all process running in docker - docker ps
11. stop container - docker stop containerId
12. to check container that are not running - docker ps --filter status="exited"
13. remove container - docker rm containerId
14. docker remove image - docker rmi imageId

