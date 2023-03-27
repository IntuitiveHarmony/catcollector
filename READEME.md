# Cat Collector

This is a walk through on creating a Django project.

## Create the database for the project.  

We will be using Posgresql for this and they have a handy command for creating a database directly from the terminal

In the terminal run:

```
createdb catcollector
```

Open the Postgres shell in the terminal by running: `psql`.  Once the shell is open, run `\l` to list all the databases. There should be a database called `catcollector`

## Start the Django Project

Navigate to the folder that will house the project.  

In the terminal run:

```
django-admin startproject catcollector
```

## Create the App

In theterminal run:
```
python3 manage.py startapp main_app
```

This will create the `main_app` folder within our project.  We need to add `main_app` to the `INSTALLED-APPS` list within our `settings.py` file.

```python
INSTALLED_APPS = [
	'main_app', # Add this line
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
]
```

## Connect to the Database




