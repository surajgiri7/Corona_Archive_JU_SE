# SE-Sprint01-Team18  

#### Members: Saad Aboujid, Keagan Holmes

The project was created based on the requirements listed in this [document](https://github.com/Magrawal17/SE-Sprint01-Team18/files/8215663/ProjectDesign.pdf).  
This project is titled "Corona Archive" and allows users to check in to locations via a QR code and be marked as infected by a hospital, along with some other functionality.

### How to set this up on your own computer:
1. Install [Python](https://www.python.org/downloads/) ver >= 3.9.0  

2. Install MariaDB 10.6.x on your machine ([for Windows here](https://mariadb.org/download/?t=mariadb&p=mariadb&r=10.6.7&os=windows&cpu=x86_64&pkg=msi&m=wilhelm))  
  NOTE: On Windows, it is encouraged that you add MySQL to PATH:
        By default, the folder should be ```C:\Program Files\MariaDB 10.6\bin```  
        Alternatively, use the MySQL Client terminal

3. Clone this GitHub repository onto your computer  

4. Change into the folder's directory and run the following command:  
``` $ pip install requirements.txt ```

5. Start the Flask server (given code is using the Bash terminal. For others, check [here](https://flask.palletsprojects.com/en/2.0.x/quickstart/):  
```
$ cd server
$ export FLASK_APP=server
$ flask run
 * Running on http://127.0.0.1:5000/
 ```
 For testing purposes, it is also possible to run the server.py file:
 ```
 $ cd server
 $ python server.py
  * Running on http://127.0.0.1:5000/
 ```

6. Access the site in your browser by connecting to the [localhost](http://127.0.0.1:5000/) connection (output after starting the Flask server)

### Sprint 1 updates

- Implemented a dashboard for the webservice  
    ✅ responsive navigation bar  
    ✅ Ability to access :   Dashboard + Scan QR Code + Notifications + Analytics + Imprint page + Settings + Search + Logout - from the navigation bar  
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
- Implemented tests that can be run with ```$ pytest -q tests.py``` in the /server directory

# SE-Sprint02

#### Members : Matias Merko,Ankel Lazaj

## IMPORTANT NOTE: All the sprint 2 work is located inside "se02" folder, the rest of the folders are from sprint 1

## Problems from the last team:

- The /register app.route has both login and registration for every user, which makes no sense
- Very messy folder organisation.
- All their css was inside one file "style.css" which is not practical
- Used so many css libraries found online, it was hard to edit the frontend and resulted to many problems.
- Different tables for agents and visitors, which make the registration harder. (We merged them into a table named User)
- Only the "register" and "login" frontend pages were implemented, the rest was missing (ex: qr scanner, qr generator, hospital page,agent page etc...)
- Flask application did not work properly

## Project changes and additions
 - Rearranged the folders:
  ```
  se02
├── app.py
├── requirements.txt
├── sql
│   └── initTables.sql
├── static
│   ├── css
│   │   ├── addhospital.css
│   │   ├── agent_page.css
│   │   ├── agentaccesspages.css
│   │   ├── displayqr.css
│   │   ├── hospital_page.css
│   │   ├── login_register.css
│   │   ├── owner_page.css
│   │   ├── scan_page.css
│   │   ├── style.css
│   │   ├── timer.css
│   │   └── visitedplacesaccess_page.css
│   ├── images
│   │   ├── anonymous.png
│   │   ├── favicon.png
│   │   └── full-logo.png
│   └── javascript
│       ├── main.js
│       ├── qrcode.js
│       ├── qrcode.min.js
│       └── reg.js
├── templates
│   ├── Placeowner_Registration.html
│   ├── Visitor_Registration.html
│   ├── addhospital_page.html
│   ├── agent_page.html
│   ├── allhospitalsaccess_page.html
│   ├── allplacesaccess_page.html
│   ├── allusersaccess_page.html
│   ├── base.html
│   ├── displayqrcode.html
│   ├── hospital_page.html
│   ├── imprint.html
│   ├── login.html
│   ├── owner_page.html
│   ├── scan_page.html
│   ├── timer.html
│   └── visitedplacesaccess_page.html
└── tests.py
  ```
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

# Guide for running the app

## Environment Creation

  ```
  virtualenv -p python3 env
  source ./env/bin/activate
  pip list
  pip freeze >requirements.txt
  ```
  
## MySql setup
  - First install MySql on your pc (Watch the *[Tutorial Guide](https://youtu.be/oxToe-4c6OM)*)
  - Run the server before accessing your database
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
    OR (make sure you put your IPv4 in the host of main of app.py)
    ```
    python3 app.py
    ```
## Python testing
  - Go to the ProjectPath
  - Run the python file named "test.py"
  ```
  python3 tests.py
  ```




