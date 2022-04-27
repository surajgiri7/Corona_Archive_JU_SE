# SE-Sprint03-Team18

MANAGIT is an application which aims to track Corona Infections via contact tracing. We aim to do this by registering people when they enter a business in collaboration with business owners, marking people as infected in collaboration with hospitals, and contacting people who are likely to have infection with the help of our admins.

## Table of content

1. [Authors](#a)
2. [Features](#f)
3. [Built with](#bw)
4. [Getting started](#gs)
5. [File Structure](#fs)
6. [Dummy Data](#dd)
7. [Installation Guide](#ig)
8. [Implementation](#i)
9. [Updates from Previous Sprint!](#up)

## <a name="a">Authors</a>

1. Sprint 1

   - Saad Aboujid
   - Keagan Holmes

2. Sprint 2

   - Matias Merko
   - Ankel Lazaj

3. Sprint 3
   - Antonia Savu
   - Suraj Giri

## <a name="f">Features</a>

- Registration for **visitors** and **business owners**
- Login for **visitors**, **business owners**, **hospitals**, and **agents**
- **Agents** can add **hospitals**, see the data about all **hospitals**, **visitors**, **places**
- **Hospitals** can update the **infection status of Visitors**
- **Visitors** can scan or upload the **QR Code** of a place
- **Owners of a Place** can generate **QR Codes** for their places.

## <a name="bw">Built with</a>

- HTML
- Javascript
- CSS
- Python3
- Flask

# <a name="gs">Getting Started</a>

To run this application, you need to follow the following steps.\
First of all, you need to have python3 nd pip installed. You can find python installation guide [here](https://www.python.org/downloads/) and pip installation guide [here](https://pip.pypa.io/en/stable/installation/). \
Once python and pip are installed, there are various python modules that are also required. \
Before we can install these modules, we need to create a virtual environment to run Flask. Follow the steps [here](https://flask.palletsprojects.com/en/2.0.x/installation/) to create a virtual environment in our application's working directory. <br>

## <a name="fs">File Structure</a>

    se-03-team-18
    ├── README.md
    ├── requirements.txt
    ├── .gitignore
    ├── sql
    │   └── initTables.sql
    ├── static
    │   ├── css
    │   │   ├── addhospital.css
    │   │   ├── agentaccesspages.css
    │   │   ├── agent_page.css
    │   │   ├── displayqr.css
    │   │   ├── hospital_page.css
    │   │   ├── login_register.css
    │   │   ├── owner_page.css
    │   │   ├── scan_page.css
    │   │   ├── style.css
    │   │   ├── timer.css
    │   │   └── visitedplacesaccess_page.css
    │   ├── images
    │   │   ├── anonymous.png
    │   │   ├── favicon.png
    │   │   └── full-logo.png
    │   └── javascript
    │       ├── main.js
    │       ├── qrcode.js
    │       ├── qrcode.min.js
    │       └── reg.js
    ├── templates
    │   ├── 404.html
    │   ├── addhospital_page.html
    │   ├── agent_page.html
    │   ├── allhospitalsaccess_page.html
    │   ├── allplacesaccess_page.html
    │   ├── allusersaccess_page.html
    │   ├── base2.html
    │   ├── base.html
    │   ├── displayqrcode.html
    │   ├── hospital_page.html
    │   ├── imprint.html
    │   ├── index.html
    │   ├── login.html
    │   ├── owner_page.html
    │   ├── Placeowner_Registration.html
    │   ├── scan_page.html
    │   ├── timer.html
    │   ├── visitedplacesaccess_page.html
    │   └── Visitor_Registration.html
    └── tests.py

## <a name="dd">Dummy Data</a>

Following is the dummy data that one can use to test the rinning of the program. <br>

### Visitor

    usename: visitor1
    password: password

### Place Owner

    usename: place1
    password: password

### Hospital

    usename: hospital1
    password: password

### Agent

    usename: aa
    password: aa

# <a name="ig">Installation Guide</a>

Following is the step by step procedure to run this application in your local device. <br>
We tried hosting the application on CLAMV but unfortunately we were unable to make it run on CLAMV.

First of all, clone the repository. <br>
`git clone https://github.com/Magrawal17/se-03-team-18.git`

Aftet that go (cd) to the project folder. <br>
`cd se-03-team-18`

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
    mysql> source sql/initTables.sql
    mysql> exit

### Note:

Before running the application, use the respective password for your own MYSQL database in line 10 of file app.py. Currently, I have written password for my device. <br>

### Once all the packages are installed, run the following command in the same command line

    export FLASK_APP=app.py
    flask run

Then, open http://127.0.0.1:5000/ in your web browser to view our application.

To run tests:

    python tests.py

## <a name="i">Implementation</a>

We implemented the frontend of our application using HTML, Javascript, and CSS. No external frameworks or libraries were used in this application. The backend was implemented using Flask.

## <a name="up">Updates in the Sprints!</a>

## Sprint 1 updates

- Implemented a dashboard for the webservice  
   ✅ responsive navigation bar  
   ✅ Ability to access : Dashboard + Scan QR Code + Notifications + Analytics + Imprint page + Settings + Search + Logout - from the navigation bar  
   ✅ navigation bar functionnalities can be accessed either by hovering over icons, or by clicking on the menu icon which opens the nav bar  
   ✅ Professionnal logo for the webservice (we have decided to call it MANAGIT) appears in the dashboard  
   ✅ logout functionnality simply by clicking on the logout icon in the bottom left

Additionally:

- Implemented an Imprint page
- Implemented the login page
- Implemented a register page for Visitors
- Implemented a register page for Place owners
- Implemented a Landing page for users to identify themselves as either visitors - place owners - hospitals or agents
- Implemented web server
- Implemented SQL database + scripts
- Implemented error management in the server file
- Implemented custom exceptions in server/exceptions.py
- Implemented tests that can be run with `$ pytest -q tests.py` in the /server directory

## Sprint 2 Updates

### Problems from the last team:

- The /register app.route has both login and registration for every user, which makes no sense
- Very messy folder organisation.
- All their css was inside one file "style.css" which is not practical
- Used so many css libraries found online, it was hard to edit the frontend and resulted to many problems.
- Different tables for agents and visitors, which make the registration harder. (We merged them into a table named User)
- Only the "register" and "login" frontend pages were implemented, the rest was missing (ex: qr scanner, qr generator, hospital page,agent page etc...)
- Flask application did not work properly

## Project changes and additions

- Rearranged the folders:
- The visitors and placeowners are able to register
- There is validation of the users that try to register
- Agents and Hospitals are able to log in (if the database has been filled with their accounts)
- After logging in, the visitors are directed to the scanning page
- After logging in, the placeowners are directed to the QRcode generating page
- After logging in, the agents are directed to the agent page
- After logging in, the hospitals are directed to the hospital page
- Visitors scan the qrcode, then they are sent to a timer website where they have the option to "leave"
- The database gets updated with visitors entering/leaving places
- Agents can :
  - Search for Visitors and Place owners
  - Add new hospital accounts
  - Search for places
  - Search for people who have visited certain places with the option of a time interval
- Hospitals can see a table with all the visitors, they can mark them infected or not infected through checkboxes
- Hospitals are able to search for specific users
- Place owners are able to register a place and a QR code for that place will be generated
- The generated QRcode for places is downloadable
- Changed the database with the necessary tables (using MySql)
- Added tests for the functionality of the website
- Updated the requirements.txt file

## Sprint3 Updates

- [x] Updated the databse for the hashed values.
- [x] Passwords are now hashed.
- [x] Added the homepage to the project.
- [x] Session management was implemented for each usertype.
- [x] LogOut funtion was implemented as it was missing.
- [x] Added back buttons to all the pages and implemented CSS for them.
- [x] Updated the CSS for the tables inside **Agent Login**, tables that were usd for accessing all the data by the agent.
- [x] Session management for preventing traversing through URL was implemented.
- [x] Implemented the prevention of entering another page through URL.
- [x] Leave Button from the page where the user is checked ina at a place now works properly.
- [x] There is now a back to home button from the QR code page.
- [x] Added foreign key PlaceID in the Visitor to Places table.
- [x] Implemented the imprint.
- [x] See all items now actually works in ALL Admin pages
- [x] Using a dynamic SQL query, it is now possible to have all combinations of parameters for searches in Admin -> visitedplaceaccess ( search by name,place,exitdate; search just by entrydate; search by all etc.)
- [x] Added tests for post methods in the unit testing.
- [x] Unit tests for visitor register success and owner register success stating on line 45 and line 74 work for a credential only once. If you want to check the same tests again, you need to change the credentials.
- [x] Routes , buttons and basic css are now implemented for tracking infections from a user
- [x] Autocomplete suggestions are now available with entries from the database in all the functions of the agent
- [x] Implemented partials search results (Auto-Complete) on all of the function in the agent page
- [x] Overall GUI Improvements

## Note: the QR code downloaded is in the form of html document. you need to open it to decode and view the QR code, which can be downloaded in the form of a .png image.

## Note2: If you are using Visual Studio Code, you might see some error messages in the Jquery used for autocomplete. The code has no errors, but VSCode Intellisense views the JavasScript syntax as wrong.That's because the correct values (from the templates) are put in at runtime, which makes it a correct JavaScript.
