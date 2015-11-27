# NGOfinder
This application is aimed at mapping all the NGOs in Delhi on the map. 
It currently supports Python 2.7 and Django 1.8.

##Installation 
Mysql should already be installed as this app uses mysql database.
To recursively install the dependencies on linux, run "**pip install -r requirements.txt**" from the terminal.
Cryptography needs libffi, therefore, if it is not present, run "**sudo apt-get install libffi-dev**" from the terminal in Ubuntu.

##Usage
Clone the repo and follow the following steps to provide required settings:
* Fill the config_template.py and secret_settings_template.py with the required parameters.
* Rename "config" to "config_template" in parse_fields.py.
* Remname "secret_settings" to "secret_settings_template" in settings.py and createDB.py.

Steps to store information in the database:
* Execute createDB.py from the terminal to create a database named "ngo".
* Run "python manage.py migrate" from mysite/ directory on the terminal.
* Run "python manage.py populate writeDB" from mysite/ directory on the terminal.

Once the database is written, run "**python manage.py runserver**" to run the django server at localhost.
