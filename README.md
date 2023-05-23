## Development setup

Install required system packages:

    sudo apt-get install python3-pip
    sudo apt-get install python3-dev python3-setuptools
    sudo apt-get install libpq-dev
    sudo apt-get install postgresql postgresql-contrib

Create www directory where project sites and environment dir

    mkdir /var/www && mkdir /var/envs && mkdir /var/envs/bin

Install virtualenvwrapper

    sudo pip3 install virtualenvwrapper
    sudo pip3 install --upgrade virtualenv

Add these to your bashrc virutualenvwrapper work

    export WORKON_HOME=/var/envs
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
    export PROJECT_HOME=/var/www
    export VIRTUALENVWRAPPER_HOOK_DIR=/var/envs/bin
    source /usr/local/bin/virtualenvwrapper.sh

Create virtualenv

    cd /var/envs && mkvirtualenv --python=python3 help_gamblers

Install requirements for a project.

    cd /var/www/help_gamblers && pip install -r requirements/local.txt

## Database creation

### For psql

    sudo su - postgres
    psql
    DROP DATABASE IF EXISTS help_gamblers;
    CREATE DATABASE help_gamblers;
    CREATE USER help_gamblers_user WITH password 'root';
    GRANT ALL privileges ON DATABASE help_gamblers TO help_gamblers_user;

## RUN Django app with main method

    python manage.py runserver

## OR

## Install Docker and docker-compose.

### Run this:

    ```bash
    docker-compose -f local.yml build
    docker-compose -f local.yml up -d
    ```

## OR

### Run django server with gunicorn
    python manage.py loaddata fixtures/countries_data.json
    python manage.py loaddata fixtures/languages_data.json
    python manage.py loaddata fixtures/casino_data.json

    currency
    ./manage.py currencies --import=USD --import=EUR
    ./manage.py updatecurrencies oxr --base=USD


    gunicorn help_gamblers_backend.wsgi --bind 0.0.0.0:55000 --workers=1 --chdir=../help_gamblers --reload

### Swagger documentation

    {host}:{port}/swagger/
    {host}:{port}/redoc/
