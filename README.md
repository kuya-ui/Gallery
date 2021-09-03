#  Gallery project
#### A simple site on how one can showcase there Gallery
#### MAXMILLAN KUYA
## Description
A site that allows people to view different images from different categories

### setup instructions
Requirements

1. Clone the repository
* Clone the the repository by running

* git clone https://github.com/kuya-ui/Gallery or download a zip file of the project from github

* Navigate to the project directory

* cd GALLERY

2. Create a virtual environment
* Install Virtualenv pip install virtualenv

* To create a virtual environment named virtual, run virtualenv virtual

* To activate the virtual environment we just created, run source virtual/bin/activate

3. Create a database
You'll need to create a new postgress database, Type the following command to access postgress

$ psql

* Then run the following query to create a new database named gallery

4.create database Galleria
5.Install dependencies
* To install the requirements from requirements.txt file,

* pip install -r requirements.txt
6.Create Database migrations
* Making migrations on postgres using django

* python3 manage.py makemigrations gallery

* then run the command below;

* python3 manage.py migrate

7.Run the app
* To run the application on your development machine,

* python3 manage.py runserver



## Known Bugs
No known bugs yet
## Technologies Used
* Python version 1.11.0.
* Django
* Bootstrap.
* PSQL database.
* HTML,CSS
## Support and contact details
* kuyamaxmillan@gmail.com
### License
[MIT Licence](https://choosealicense.com/licenses/mit/)

Copyright (c) 2021 Maxmillan Inc.