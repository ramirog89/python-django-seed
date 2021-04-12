python-django-seed
===================
Working example of [django-rest-framework](https://github.com/tomchristie/django-rest-framework/tree/master)
JWTAuthentication with simpleJwt ([rest_framework_simplejwt](https://github.com/davesque/django-rest-framework-simplejwt))

## Requirements 
* You should have [virtualenv](http://www.virtualenv.org/en/latest/#installation) installed. 
* You should have [pip](https://pypi.org/project/pip/) installed.

## Install 
Clone this repo, set up and activate a virtualenv:
```console
git clone git@github.com:ramirog89/django-rest-seed.git
cd django-rest-seed
virtualenv env
source env/bin/activate
```

Setup dependencies:
```console
make install
```

```console
make initdb
python manage.py createsuperuser --username {username}
```

## Run the server:development
```console
make dev
```

## Run the server:production
```console
make prod
```

Launch [http://localhost:8000](http://localhost:8000) in your browser.

## Tests 
```console
make test 
```
