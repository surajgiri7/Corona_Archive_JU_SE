# README - CORONA ARCHIVE
Corona Archive is an application which aims to track Corona Infections via contact tracing. We aim to do this by registering people when they enter a business in collaboration with business owners, marking people as infected in collaboration with hospitals, and contacting people who are likely to have infection with the help of our admins. 


## Table of content
1. [Authors](#a)
2. [Features](#f)
3. [Built with](#bw)
4. [Getting started](#gs)
5. [Implementation](#i)
6. [File Structure](#fs)
7. [Application status](#as)
8. [Future updates](#fu)
9. [References](#r)

## <a name="a">Authors</a>
1. Sprint 1
    * Abhishek Ojha
    * Suraj Giri

## <a name="f">Features</a>
- Registration for **visitors** and **business owners**
- Login for **visitors**, **business owners**, **hospitals**, and **agents**
- **Agents** can add **hospitals**


## <a name="bw">Built with</a>
* HTML
* Javascript
* CSS
* Python3
* Flask

## <a name="gs">Getting Started</a>
To run this application, you need to follow the following steps.\
First of all, you need to have python3 nd pip installed. You can find python installation guide [here](https://www.python.org/downloads/) and pip installation guide [here](https://pip.pypa.io/en/stable/installation/). \
Once python and pip are installed, there are various python modules that are also required. \
Before we can install these modules, we need to create a virtual environment to run Flask. Follow the steps [here](https://flask.palletsprojects.com/en/2.0.x/installation/) to create a virtual environment in our application's working directory. <br>

Following is the step by step procedure. <br>

Install flask: <br>
    ```pip install flask```

Install Virtual Environment .\
    ```pip install virtualenv```

create the Virtual Environment .\
    ```virtualenv env```

### Start the virtual environment.
### for mac and linux
    
    source env/bin/activate

### for windows

    env\Scripts\activate 

Once the terminal with the virtual environment in our application's working directory is ready, enter the following commands to install the required packages.

    pip install flask-sqlalchemy
    pip install flask-wtf
    pip install flask-bcrypt
    pip install flask-login
    pip install email_validator



Once all the packages are installed, run the following command in the same command line

    export FLASK_APP=run.py
    flask run

Then, open http://127.0.0.1:5000/ in your web browser to view our application.

To run tests:

    python test_app.py

## <a name="i">Implementation</a>
### Sprint 1
We implemented the frontend of our application using HTML, Javascript, and CSS. No external frameworks or libraries were used in this application. The backend was implemented using Flask.

## <a name="fs">File Structure</a>
	\main 	(github's branch)
	
		\run.py

        \test_app.py
		
		\corona
		
			\static
			
				\....	(CSS files and Images' folder)
			
			\templates
			
				\....	(HTML files)	
			
			\__init.py__	
			
			\corona.db
			
			\forms.py	(includes the forms created within flask)
			
			\models.py	(includes the database created)
			
			\routes.py	(includes the routes to various pages)
		
		\test_main.py
		
		\environments\env	(created during installation of env)
		
			\...		(several files required for env)    
		
		\database.txt   (if you need to access the database from the terminal(CLI))
			
## <a name="as">Applicaiton status</a>
* Created the frontend (GUI Pages) for all different pages for login, registration and verification using HTML, CSS and Javascript.
* Created the database using SQLite.
* Created various forms for login and register of users and places using flask-wtforms in forms.py.
* Created the login of the Agent, who only after registration, can create accounts for the hospitals.(We were firstly planning on creating a  register route for hospital though registration page but later on we followed the advice from Professor that only agents can create the accounts for hospitals.)
* Created thte database model in models.py
* Created routes to all the pages in routes.py
* Worked on Authentication with flask_login.
* Finally created a testing page with testcases for various pages and functions in our applicaton.
* Currently all the visitors are marked Negative for the infected attribute in the database
* We also used flask-bcrypt to hash the passwords so that noone else except the one who entered the password would be able to access the password.

## <a name="fu">Future updates</a>
* Generate a QR code for business owners
* Scan QR code to enter a business (We tried on creating a QR Scanner after a user clicks on the Scan QR button on the homepage but but we could not complete it due to time constraints. The partial code for the QR scanner could be found on the ./templates/afterLogin/scanQRcode.html)
* Hospitals can mark users as infected

## <a name="r">References</a>
Testing
- https://www.youtube.com/watch?v=iQVvpnRYl-w&t=261s&ab_channel=MVPEngineer
- https://www.youtube.com/watch?v=6tNS--WetLI&t=464s&ab_channel=CoreySchafer
