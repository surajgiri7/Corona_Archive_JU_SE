from flask import Flask, render_template, request, session
from flaskext.mysql import MySQL
import os
from exceptions import *

#########################################################
''' @README @TODO @CHANGE

    To set up the server to run on your machine use find (ctrl+f)
    and search for "@CHANGE". This will highlight parts of the code
    that must be edited for the server to properly function

    To start the server simply run this python file:
    $ python server.py
'''
#########################################################

''' ### FLASK SERVER SETUP ### '''

# This code gets the absolute directory for the /../frontend/ folder
root_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
root_dir = os.path.join(root_dir, 'frontend')
# /frontend/static/
static_dir = os.path.join(root_dir, 'static')

# Flask app https://flask.palletsprojects.com/en/2.0.x/
app = Flask(__name__.split('.')[0], root_path=root_dir, template_folder=root_dir, static_folder=static_dir)
app.secret_key = os.urandom(32)

''' @CHANGE
    
    ### SQL DATABASE SETUP ###

    Update user, password, and database
'''
try:
    # default credentials are user: "root" password: "root"
    app.config['MYSQL_DATABASE_USER']     = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'passwd'
    # default port is 3306
    app.config['MYSQL_DATABASE_PORT']     = 3306
    app.config['MYSQL_DATABASE_DB']       = 'Group18'
    app.config['MYSQL_DATABASE_HOST']     = 'localhost'

    mysql = MySQL()
    mysql.init_app(app)

    db_connection = mysql.connect()
    cursor = db_connection.cursor()
except:
    raise DatabaseError

#########################################################

''' ### REQUESTS HANDLING ### '''

# For help with requests, see: https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask


@app.route("/", methods=['GET'])
def index():
    return render_template('homepage.html')

@app.route("/imprint", methods=['GET'])
def imprint():
    return render_template('imprint.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']

            cursor.execute("SELECT * FROM Visitors V, Hospitals H, Agents A WHERE (V.VisitorUsername={username} AND V.VisitorPassword={password}) OR (H.HospitalUsername={username} AND H.HospitalPassword={password}) OR (A.AgentUsername={username} AND A.AgentUsername={password})")

            print("Cursor ok")

            n = cursor.rowcount
            data = cursor.fetchall() # Ensure cursor is still usable after this query
            db_connection.commit()
            
            print(n)

            # Check if login was successful
            if n == 1:
                return render_template('index.html') # Login successful @TODO add session id/info
            elif n > 1:
                raise LoginError
            elif n < 1:
                raise UserPassNotFound

        except LoginError:
            return render_template('login.html', msg=LoginError.message)
        except UserPassNotFound:
            return render_template('login.html', msg=UserPassNotFound.message)
        except:
            return render_template('login.html', msg=UnknownError.message)

    return render_template('login.html')

# @TODO
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            name     = request.form['name']
            address  = request.form['address']
            phone    = request.form['phone']
            email    = request.form['email']
            did      = 0                        # @TODO Figure out a way to get a unique device ID. Temp solution is set it = 0 for all devices

            if not email and not phone:
                return render_template('register.html', msg="You must input either your phone number, email, or both")

            # Make sure username is not taken
            cursor.execute("SELECT * FROM Visitors V, Hospitals H, Agents A WHERE V.VisitorUsername={username} OR H.HospitalUsername={username} OR A.AgentUsername={username}")
            username_check = cursor.fetchall()
            db_connection.commit()
            if username_check:
                raise UsernameTakenError

            cursor.execute("INSERT INTO Visitors (VisitorName, VisitorAddress, VisitorPhoneNumber, VisitorEmail, VisitorDeviceID, VisitorUsername, VisitorPassword) VALUES ({name}, {address}, {phone}, {email}, {did}, {username}, {password})")
            db_connection.commit()

            # Make sure data was put into the database:
            cursor.execute("SELECT * FROM Visitors WHERE VisitorUsername={username} AND VisitorPassword={password}")
            visitor_check = cursor.fetchall()
            db_connection.commit()

            if visitor_check:
                return render_template('login.html', msg="Success! Please log in")
            else:
                raise UnknownError

        except UsernameTakenError:
            return render_template('register.html', msg=UsernameTakenError.message)
        except:
            return render_template('register.html', msg="Error in registration. Check input data and try again.")

    return render_template('register.html')

@app.route('/register-po', methods=['GET', 'POST'])
def register_po():
    if request.method == 'POST':
        try:
            # Place owner data
            name     = request.form['name']
            phone    = request.form['phone']
            email    = request.form['email']
            
            # Place data
            place_name    = request.form['place_name']
            place_address = request.form['place_address']

            # Check if inputted data is already in the database, cancel request if true
            cursor.execute("SELECT * FROM Places WHERE PlaceName={place_name} AND PlaceAddress={place_address}")
            place_check = cursor.fetchall()
            db_connection.commit()

            if place_check:
                raise AlreadyInDatabaseError

            # Check if owner exists in database, if not add them
            cursor.execute("SELECT PlaceOwnerID FROM PlaceOwners WHERE PlaceOwnerName={name} AND PlaceOwnerPhoneNumber={phone} AND PlaceOwnerEmail={email}")
            owner_id = cursor.fetchall()
            db_connection.commit()

            if not owner_id:
                cursor.execute("INSERT INTO PlaceOwners (PlaceOwnerName, PlaceOwnerPhoneNumber, PlaceOwnerEmail) VALUES ({name}, {phone}, {email})")
                db_connection.commit()

                cursor.execute("SELECT PlaceOwnerID FROM PlaceOwners WHERE PlaceOwnerName={name} AND PlaceOwnerPhoneNumber={phone} AND PlaceOwnerEmail={email}")
                owner_id = cursor.fetchall()
                db_connection.commit()

            # Insert Place data into Places
            cursor.execute("INSERT INTO Places (PlaceName, PlaceAddress, PlacesPlaceOwnerID) VALUES ({place_name}, {place_address}, {owner_id})")
            db_connection.commit()

        except AlreadyInDatabaseError:
            return render_template('register-po.html', msg=AlreadyInDatabaseError.message)
        except:
            return render_template('register.html', msg="Error in registration. Check input data and try again.")

    return render_template('register-po.html')



#########################################################
''' @CHANGE

    This code allows the server to be started by simply
    running this python file with the following command
    in this directory:

    $ python server.py

    If there are issues, try changing the port
'''

if __name__ == '__main__': 
    app.run(debug=True, port=5000)

# for testing purposes
def create_app():
    app = Flask(__name__)
    return app
#########################################################




