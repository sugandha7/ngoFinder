# NGOfinder
This application is aimed at mapping all the NGOs in Delhi on the map. 
It currently supports Python 2.7 and Django 1.8.
To recursively install the dependencies on linux, run "pip install -r requirements.txt" from the terminal.
Steps to store information in the database:
* Execute createDB.py from the terminal to create a database named "ngo".
* Run "python manage.py migrate" from mysite/ directory on the terminal.
* Run "python manage.py populate writeDB" from mysite/ directory on the terminal.

