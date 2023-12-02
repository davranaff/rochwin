# Django/PorstgeSql test project for Rochwin


### Create venv

```bash
>>> virtualenv venv
...
>>> source venv/bin/activate
>>> (venv) ...
```

### Install all dependencies

```bash
>>> pip3 install -r requirements.txt
```

### Change database settings

project settings are in config/settings.py

```python
# config/settings.py

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': '<db_name>',
       'USER': '<db_user>',
       'PASSWORD': '<db_password>',
       'HOST': 'localhost',
       'PORT': '5432',
   }
}
```

### Make migrations and run migrate

```bash
>>> python3 manage.py makemigrations
...
>>> python3 manage.py migrate
```

### It is important to remember that you need to add some data to the admin panel !

`http://localhost:8000/admin`

```bash 
>>> python3 manage.py createsuperuser

>>> username: <username>
>>> email: <email>
>>> password: <password>
>>> retry password: <password>

>>> successfully created !!!
```


### There are 3 endpoints

`http://localhost:8000/api/v1/statistics/employee/?month=11&year=2023`

`http://localhost:8000/api/v1/statistics/employee/1/?month=11&year=2023`

`http://localhost:8000/api/v1/statistics/client/1/?month=11&year=2023`



### Run project

```bash
>>> python3 manage.py runserver localhost:8000
```
