####### INITIALIZATION

clean:
	# find . -name '*.pyc' -exec rm --force {}
	# find . -name '*.pyo' -exec rm --force {}
	# find . -name '*~' -exec rm --force  {}
	rm -rf coverage/
	rm -r logs/*
	rm -rf *.egg-info

install:
	pip install --upgrade setuptools
	pip install --upgrade -r requirements.txt

####### DATABASE

initdb:
	python manage.py migrate

migrate:
	python manage.py makemigrations
	python manage.py migrate

####### RUN SERVER

.PHONY : start_server dev prod

local: SETTINGS = src.app.config.env.development
dev:   SETTINGS = src.app.config.env.development
prod:  SETTINGS = src.app.config.env.production
test: SETTINGS = src.app.config.env.test

local dev prod:
	python3.8 manage.py runserver 0.0.0.0:8000 --settings=$(SETTINGS)

####### TESTING

SOURCE_DIR = ./src/app

lint:
	flake8 $(SOURCE_DIR)

test:
	coverage run --source="$(SOURCE_DIR)" manage.py test src/tests/ --force-color -v 1 --settings=$(SETTINGS)
	coverage html -d coverage
	coverage report -m
	coverage erase

####### BUILD / DEPLOY

check:
	python manage.py check --deploy
