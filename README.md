# VMS - Sivakashi Django Rest API

This is the Visitor Management System API built with Django Rest Framework.

# **Getting Started 🚦**

**Clone the repo**

    git clone git@github.com:thubamamba/vms_django_rest_api.git

**Initializing the app 🔨**

First you need to edit your hosts file in your machine add the following line.

    127.0.0.1       sivakashi.com

You can do this on mac by running this command:

    sudo nano /etc/hosts

**Installing the requirements 📦**

Then you need to create a virtual environment and activate it.

    python3 -m venv venv
    source venv/bin/activate

Then you need to install the requirements.

    pip install -r requirements.txt

Then you need to run the migrations.

    python manage.py migrate --settings=vms_django_rest_api.settings_dev

Then you need to create a superuser.

    python manage.py createsuperuser --settings=vms_django_rest_api.settings_dev

Then you need to run the server.

    python manage.py runserver --settings=vms_django_rest_api.settings_dev

Whenever you create an account in order to access it you need to append the hosts file with following pattern

    127.0.0.1       [account_username].sivakashi.com

**Running the tests 🧪**
    
        python manage.py test --settings=vms_django_rest_api.settings_dev

**Authentication 🚪**

We use JWT for authentication. 

**Signing Up**

    http://[subdomain].sivakashi.com:8000/auth/signup/

**Logging In**
    
        http://[subdomain].sivakashi.com:8000/auth/login/

**Refreshing the token**

    http://[subdomain].sivakashi.com:8000/auth/refresh/token/