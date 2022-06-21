# SE-Sprint01-Team19

## Table of content

1. [Authors](#a)
2. [Features](#f)
3. [Built with](#bw)
4. [Getting started](#gs)
5. [File Structure](#fs)
6. [Dummy Data](#dd)
7. [Installation Guide](#ig)
8. [Implementation](#i)
9. [Project Progress](#pp)

## <a name="a">Authors</a>

### Sprint 1:
  - Matias Merko 
  - Bidur Niroula

### Sprint 2:
  - Keagan Holmes
  - Antonia Savu

### Sprint 3:
  - Ankel Lazaj

### Sprint 4:
  - Suraj Giri
  - Zixiang Wang

## <a name="f">Features</a>
- Visitors can register themselves into the database application.
- Place owners can register themselves into the database of the application.
- Agent login Credentials are hard-written into the database so that they ara not able to register themselves.
- Agents can add hospitals
- Agents can see the analytics about the functioning of the application.
- Hospitals can update the infection status of patients.
- The entry date-time and exit date-time of patient is stored into the database.
- Agent can access the analytics as per different provided search methods.

## <a name="bw">Built With</a>
- HTML
- Javascript
- CSS
- Python3
- Flask

## <a name="gs">Getting Started</a>
To run this application, you need to follow the following steps.\
First of all, you need to have python3 nd pip installed. You can find python installation guide [here](https://www.python.org/downloads/) and pip installation guide [here](https://pip.pypa.io/en/stable/installation/). \
Once python and pip are installed, there are various python modules that are also required. \
Before we can install these modules, we need to create a virtual environment to run Flask. Follow the steps [here](https://flask.palletsprojects.com/en/2.0.x/installation/) to create a virtual environment in our application's working directory. <br>

## <a name="fs">File Structure</a>

    se-04-team-19
    ├── README.md
    ├── requirements.txt
    ├── sql
    │   └── se_db.sql
    ├── static
    │   ├── css
    │   │   ├── agentAddHospital.css
    │   │   ├── agentPage.css
    │   │   ├── analyticsPages.css
    │   │   ├── displayqr.css
    │   │   ├── hospitalPage.css
    │   │   ├── login.css
    │   │   ├── owner_page.css
    │   │   ├── registration.css
    │   │   ├── scan_page.css
    │   │   ├── style.css
    │   │   ├── timer.css
    │   │   └── yourein.css
    │   ├── images
    │   │   ├── background.jpg
    │   │   ├── covid.jpeg
    │   │   ├── covid_vaccine.jpeg
    │   │   ├── favicon-16x16.png
    │   │   ├── favicon-32x32.png
    │   │   ├── favicon.ico
    │   │   ├── hospital.png
    │   │   ├── login.jpg
    │   │   ├── place.png
    │   │   ├── QR-Code.png.crdownload
    │   │   ├── registration.jpg
    │   │   └── stats.png
    │   └── javascript
    │       ├── formValidation.js
    │       ├── hospitalAction.js
    │       ├── markVisitor.js
    │       ├── qrcode.js
    │       └── qrcode.min.js
    ├── templates
    │   ├── 404.html
    │   ├── agentPage.html
    │   ├── allHospitalsAnalytics.html
    │   ├── allPlacesAnalytics.html
    │   ├── allUserAnalytics.html
    │   ├── allVisitedAnalytics.html
    │   ├── base.html
    │   ├── displayqrcode.html
    │   ├── foooter.txt
    │   ├── hospitalPage.html
    │   ├── hospitalRegister.html
    │   ├── imprint.html
    │   ├── login.html
    │   ├── owner_page.html
    │   ├── Place_owner_registration.html
    │   ├── scan_page.html
    │   ├── timer.html
    │   ├── trackEachInfect.html
    │   ├── trackPossibleInfect.html
    │   ├── Visitor_Registration.html
    │   └── yourein.html
    └── test.py

## <a name="dd">Dummy Data</a>
### Visitors:
- Username: visitor1
- password: password

### Place Owners:
- Username: place1
- password: password

### Hospitals:
- Username: hospital1
- password: password

### Agent:
- Username: agent
- password: password

## <a name="ig">Installation Guide</a>
Following is the step by step procedure to run this application in your local device. <br>
We tried hosting the application on CLAMV but unfortunately we were unable to make it run on CLAMV.

First of all, clone the repository. <br>
`git clone https://github.com/Magrawal17/se-04-team-19.git`

Aftet that go (cd) to the project folder. <br>
`cd se-04-team-19`

Install flask: <br>
`pip install flask`

Install Virtual Environment .\
 `pip install virtualenv`

create the Virtual Environment .\
 `virtualenv env`

### Start the virtual environment.

### for mac and linux

    source env/bin/activate

### for windows

    env\Scripts\activate

Once the terminal with the virtual environment in our application's working directory is ready, enter the following commands to install the required packages.

    pip install -r requirements.txt

## Generation of the database

### You will also need a MYSQL database for this project. To create one, follow the following steps

    # Open MYSQL [inside the project folder (.../se-03-team-18/)]
    $ mysql -u {Enter your username or ROOT} -p
    Enter your password: {your password here}

    # Once you are in your MYSQL terminal, run this command for creating the db.
    mysql> source sql/se_db.sql
    mysql> exit

### Note:

### Before running the application, use the respective password for your own MYSQL database in line 39 of file app.py. Currently, I have written password for my device. <br>

### Once all the packages are installed, run the following command in the same command line

    export FLASK_APP=app.py
    flask run

Then, open http://127.0.0.1:5000/ in your web browser to view our application.

To run tests:

    python tests/test.py


## <a name="pp">Project Progress</a>
 - The visitors and placeowners are able to register
 - There is validation of the users that try to register
 - After logging in, the visitors are directed to the scanning page
 - After logging in, the placeowners are directed to the QRcode generating page
 - The generated QRcode is downloadable
 - Agents and Hospitals are able to log in (if the database has been filled with their accounts) 
 - Added tests for the functionality of the website
 - Made a requirements.txt file
 - Created database with the necessary tables (using MySql) 

# Installation guide

## Environment Creation
	module cv2
	module pyzbar

  ```
  virtualenv -p python3 env
  source ./env/bin/activate
  pip list
  pip freeze >requirements.txt
  ```
  
## MySql setup
  - First install MySql on your pc (Watch the *[Tutorial Guide](https://youtu.be/oxToe-4c6OM)*)
  - Access database:
      ```shell
      mysql -u root -p
      Enter password: 
      # Please enter the password you put into your mysql database
      ```
  - In the app.py file, please write your password for the MySql database
 
## Running the code step by step
  - Go to the project folder
    ```
    cd PATH/TO/PROJECT
    ```
  - Do the environment creation steps shown above
  - Activate the environment
  - In the terminal write:
    ```
    export FLASK_APP=app.py
    flask run
    ```

  - To tun the program in debugger mode:
    ```
    python app.py
    ```

## Python testing
  - Run the python file named "test.py":

    ```
    python test.py
    ```

---------------------------------------------------------------

## Sprint 2 Updates:
  - Code now contains meaningful comments throughout.
  - Implemented session management. Pages which require authentification cannot be accessed without a session. Both login and logout actions are functional. 
  - Changed database structure in order to allow for different function implementations.
  - There is now a registration page for hospitals.
  - There is now a functional login page for hospitals AND agents.
  - Created a main landing page for agents, where all the functions related to this role are to be implemented.
  - Agents are now able to accept or reject hospital registration requests, subsequently updating the database. Function implemented using AJAX request, such that the list of pending registration requests gets updated without the need of a refresh.
  - Created a main landing page for hospitals, where all functions related to this role are to implemented.
  - Hospitals are now able to change the infection status of a user. Similarly to the function mentioned above, we used AJAX to update the status in the browser without the need of a refresh. This of course also updates the database.
  - Passwords are now hashed (using bcrypt).
  - Some GUI improvements.
  - Create favicon.ico file (custom design), solving a 404 error.
  - Added SQL script to insert test data.
  - Added SQL script to drop tables.
  - Added additional tests and test cases. 
  - Added a route and a template which handles 404 errors.
  - All the pages now have a button which leads you back to main.

## Sprint 3 Updates:
  - Hashed function for passwords now works.
  - Updated database to record the place, entry/exit time/date of a person.
  - Added functions to update the database every time a person enters a place with the given qrcode. The exit time/date is recorded after user logs out.
  - Created a "You're in" page after the user submits the qrcode.

### Important notes:

  1. For functionality testing on the agent page, please use the following credentials : ``` Username:admin  Password:password ```
  2. A new sql dump was created, it can be found inside ```softwareengineering.sql```
  3. Hospitals can only log in if their form was accepted by an admin. To test the main page for hospitals, please make sure to use a row with the status ***accepted***.
  4. Please note that all the testcases, even the "bad" ones, return 200. This is because of the error handling inside the code, instead of throwing an error and crashing, a comment is shown to alert the user of the problem.


## Sprint 4 Updates:
  - [x] Agent Pages that were missing are added.
  - [x] File structure, that was missing before, is implemented.
  - [x] Dummy Data, previously not included, is added.
  - [x] Updated the CSS and overall UI & UX.
  - [x] All the analytics pages for the agent were added.
  - [x] Search functionalities for the analytics pages was added.
  - [x] Auto-complete feature(in search) for the analytics page for agent was added.
  - [x] Updated the SQL queries for the database as there were many queries that were not used. 
  - [x] Updated the database for hashed values.
  - [x] Updated the database with hashed passwords for dummy data.
  - [x] Hashed password for agent and the users properly implemented for all the users.
  - [x] Added back buttons to all the pages and implemented CSS for them.
  - [x] LogOut funtion was implemented prperly for all pages.
  - [x] Using a dynamic SQL query, it is now possible to have all combinations of parameters for searches in Admin -> visitedplaceaccess ( search by name,place,exitdate; search just by entrydate; search by all etc.)
  - [x] Removed unwanted .sql files
  - [x] Implemented the prevention of entering another page through URL
  - [x] Implemented the functionality of preventing access pags of another user type when loggd in as one type of user.
  - [x] Added and implement Imprint Page.
  - [x] Incorporated the login, irrespective of their usertype, into the same page. After username and password match, the respective login page is shown according to the database.
 ### Note: the QR code downloaded using download button is in the form of html document. you need to open it to decode and view the QR code, which can be downloaded in the form of a .png image.
