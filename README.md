This is the template for tendenci 7.1.

To start a new tendenci project with this template (replace `<project_name>` with your project name):

    django-admin.py startproject --template=https://github.com/tendenci/tendenci-project-template/zipball/master <project_name>


**Alright, if you're new to Tendenci and want to set it up on your local computer (Mac or Ubuntu), read on.**

Once the project template is pulled down, you can follow these steps to set it up on your local (those are pretty much the standard processes like any other django project):

###### 1) Install the requirements
    
    cd <project_name>
    pip install -r requirements/dev.txt    # ideally run it in a virtual environment with virtualenv and virtualenvwrapper
    
    
###### 2) Update conf/local_settings.py for the three settings

i) DATABASES - first create your database with postgis enabled (The psql command to enable postgis is: `CREATE EXTENSION postgis`). Then replace `<DB_NAME>`, `<DB_USER>` and `<DB_PASS>` with your database name, user and password, respectively.

ii) SECRET_KEY and SITE_SETTINGS_KEY  - each should be a random string with the length of 32. Here, we provide a little help to authmatically generate random strings and update `SECRET_KEY` and `SITE_SETTINGS_KEY` with this command:


    curl https://gist.githubusercontent.com/jennyq/45de71a93cff774c593d/raw/30ede14eb133de66cc839cc0458a1e915368534e/setup_keys.sh | bash

    
###### 3) Run the deploy script to create the database tables (Sit back and relax - the django database migration might take a while.)

    python deploy.py
    
###### 4) Populate some default data

    python manage.py load_base_defaults
    
Optionally, you can load more date with the command

    python manage.py load_npo_defaults
    
###### 5) Make sure the execute permission is removed from the media/ directory

	chmod -R -x+X media
    
###### 6) To create a superuser login, run this command and follow with the prompt

    python manage.py createsuperuser
   
###### 7) Run it!

    python manage.py runserver
    
