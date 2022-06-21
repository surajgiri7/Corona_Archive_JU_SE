
from flask import Flask, render_template, request, redirect, url_for, session, flash
import datetime
import bcrypt
import pymysql
import os

# from flask_bcrypt import Bcrypt
# from datetime import datetime

#########################################################
""" @README @TODO @CHANGE

    To set up the server to run on your machine use find (ctrl+f)
    and search for "@CHANGE". This will highlight parts of the code
    that must be edited for the server to properly function

    To start the server for testing simply run this python file:
    $ python app.py

    To start the server for production run the following:

    $ export FLASK_APP=app.py
    $ flask run

"""
#########################################################



""" @CHANGE
    
    ### SQL DATABASE SETUP ###

    Update user, password, and database
"""

db = pymysql.connect(
    host="127.0.0.1", user="root", password="@Nothing7", database="se_db"
)

""" ### FLASK SERVER SETUP ### """
app = Flask(__name__)
secret = app.secret_key = os.urandom(32)
app.secret_key = secret
# bcrypt = Bcrypt(app)

#########################################################

""" ### REQUESTS HANDLING ### """

# For help with requests, see: https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask




# imprint
@app.route("/imprint")
def imprint():
    return render_template("imprint.html")

# HOME
@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login_page():
    if session.get("account_type") == "visitor":
        return redirect(url_for("scan_page", user_name=session["account_type"]))
    elif session.get("account_type") == "owner":
        return redirect(url_for("owner_page", user_name=session["account_type"]))
    elif session.get("account_type") == "hospital":
        return redirect(url_for("hospital_page", user_name=session["account_type"]))
    elif session.get("account_type") == "agent":
        return redirect(url_for("agent_page", user_name=session["account_type"]))
    else:
        # return render_template("index.html")

# LOGIN
# @app.route("/login", methods=["GET", "POST"])
# def login_page():
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["psw"]

            with db.cursor() as cur:
                cur.execute("SELECT password from User where Username=%s", (username))
                hashpassobj = cur.fetchone()
                if hashpassobj:
                    hashpass = hashpassobj[0]
                    if bcrypt.checkpw(password.encode("utf-8"), hashpass.encode("utf-8")):
                        cur.execute(
                            "SELECT * FROM User U WHERE U.Username=%s AND U.Password=%s",
                            (username, hashpass),
                        )
                        account = cur.fetchone()
                        cur.close()
                        print(account)
                        if account:
                            # Checking if the account owner is a visitor/place owner/agent or hospital
                            if account[9] == "visitor":
                                # Visitors go to scanning page
                                session["username"] = username
                                session["account_type"] = "visitor"
                                return redirect(url_for("scan_page", user_name=account[7]))
                            elif account[9] == "owner":
                                # Owners go to owner page
                                session["username"] = username
                                session["account_type"] = "owner"
                                return redirect(url_for("owner_page", user_name=account[7]))
                            elif account[9] == "agent":
                                # Agents go to agent page
                                session["username"] = username
                                session["account_type"] = "agent"
                                print(session["account_type"])
                                return redirect(url_for("agent_page", user_name=account[7]))
                            elif account[9] == "hospital":
                                # Hospitals go to hospital page
                                session["username"] = username
                                session["account_type"] = "hospital"
                                return redirect(
                                    url_for("hospital_page", user_name=account[7])
                                )
                    else:
                        # if the account does not exist return error
                        return render_template("login.html", error=True)
                else:
                    cur.close()
                    return render_template("login.html", error=True)
        else:
            return render_template("login.html")

# SCANNING PAGE
@app.route("/scan_page/<user_name>", methods=["GET", "POST"])
def scan_page(user_name):
    if request.method == "POST":
        # Getting the info from the scanned qr code
        username = user_name
        placename = request.form["place_name"]
        placeaddress = request.form["place_address"]
        entrydate = datetime.datetime.now()
        with db.cursor() as cur:
            cur.execute("SELECT * FROM User U WHERE U.Username=%s", (user_name))
            the_user = cur.fetchone()
            cur.close()
            isinfected = the_user[6]
        try:
            # Inserting the visitor into VisitorToPlaces table, which keeps track of people visiting different places
            # Note: No exit date is entered since the visitor has just entered the place
            with db.cursor() as cur:
                cur.execute(
                    "INSERT INTO VisitorToPlaces(Visitor,Place,EntryDateTime,ExitDateTime,infected) VALUES (%s,%s,%s,%s,%s)",
                    (user_name, placename, entrydate, None, isinfected),
                )
                db.commit()
                print("new VisitorToPlaces added")
        finally:
            cur.close()
            # After scanning, visitors are sent to a page with a timer
        return redirect(
            url_for(
                "timer_page",
                user_name=username,
                place_address=placeaddress,
                place_name=placename,
            )
        )
    else:
        if session.get("account_type") == "visitor":
            return render_template("scan_page.html", Username=user_name)
        else:
            return redirect(url_for("login_page"))

# add a visitor to database from form (POST)/load the page (GET)
@app.route("/registervisitor", methods=["GET", "POST"])
def register_visitor():
    print("lolol")
    if request.method == "POST":
        name = request.form["name"]
        username = request.form["username"]
        password = request.form["psw"]
        salt = bcrypt.gensalt()
        hashpass = bcrypt.hashpw(password.encode("utf-8"), salt)
        address = request.form["address"]
        email = request.form["email"]
        phone = request.form["phone"]
        did = request.remote_addr
        infected = 0
        # CHECKING IF USERNAME IS ALREADY TAKEN
        with db.cursor() as cur:
            cur.execute("SELECT * FROM User U WHERE U.username=%s", username)
            compare = cur.fetchone()
            cur.close()
            if compare:
                return render_template("Visitor_Registration.html", usernametaken=True)
        # CHECKING IF AT LEAST EMAIL OR PHONE HAS BEEN ENTERED
        if email == "" and phone == "":
            return render_template("Visitor_Registration.html", fillerror=True)
        else:
            # INSERTING THE NEW ACCOUNT INTO THE DATABASE
            try:
                with db.cursor() as cur:
                    cur.execute(
                        "INSERT INTO User(Name,Address,PhoneNumber,Email,Username,Password,infected,Usertype,DeviceID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            name,
                            address,
                            phone,
                            email,
                            username,
                            hashpass,
                            0,
                            "visitor",
                            did,
                        ),
                    )
                    db.commit()
                print("new user inserted")
            finally:
                cur.close()
            return redirect(url_for("login_page"))
    else:
        return render_template("Visitor_Registration.html")

# Add a place owner to database from form (POST)/load the page (GET)
@app.route("/registerowner", methods=["GET", "POST"])
def register_owner():
    if request.method == "POST":
        name = request.form["name"]
        username = request.form["username"]
        password = request.form["psw"]
        salt = bcrypt.gensalt()
        hashpass = bcrypt.hashpw(password.encode("utf-8"), salt)
        address = request.form["address"]
        email = request.form["email"]
        phone = request.form["phone"]
        did = request.remote_addr
        infected = 0
        # CHECKING IF USERNAME IS ALREADY TAKEN
        with db.cursor() as cur:
            cur.execute("SELECT * FROM User U WHERE U.username=%s", username)
            compare = cur.fetchone()
            cur.close()
            # IF USERNAME IS TAKEN RETURN ERROR
            if compare:
                return render_template(
                    "Place_owner_registration.html", usernametaken=True
                )
        try:
            # INSERTING ACCOUNT INTO DATABASE
            with db.cursor() as cur:
                cur.execute(
                    "INSERT INTO User(Name,Address,PhoneNumber,Email,Username,Password,infected,Usertype,DeviceID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (name, address, phone, email, username, hashpass, 0, "owner", did),
                )
                db.commit()
            print("new place owner inserted")
        finally:
            cur.close()
        return redirect(url_for("login_page"))
    else:
        return render_template("Place_owner_registration.html")

# page where place owners can register a place(POST)/ see the form to register a place (GET)
@app.route("/owner/<user_name>", methods=["GET", "POST"])
def owner_page(user_name):
    # ensure user is logged in (session exists)
    if session.get("account_type") == "owner":
        if request.method == "POST":
            placename = request.form["placename"]
            address = request.form["address"]

            """ @CHANGE 
                Edit the IP address below to be the localhost address
            """
            qrcode = "http://127.0.0.1:5000/scan" + user_name + "/" + address + "/timer"
            with db.cursor() as cur:
                cur.execute(
                "SELECT * FROM Places P WHERE P.PlaceName=%s AND P.PlaceAddress=%s",
                    (placename, address),
                )
                place = cur.fetchone()
                cur.close()
                if place:
                    return redirect(
                        url_for(
                            "displayqr_page", 
                            placename = placename,
                            username=user_name, place_address=address
                        )
                    )
            try:
                with db.cursor() as cur:
                    cur.execute(
                    "INSERT INTO Places(PlaceName,PlaceAddress,QRcode) VALUES (%s,%s,%s)",
                        (placename, address, qrcode),
                    )
                    db.commit()
            finally:
                cur.close()
            return redirect(
                url_for("displayqr_page",placename=placename, username=user_name, place_address=address)
            )
        else:
            return render_template("owner_page.html", username=user_name)
    else:
        return redirect(url_for("login_page"))


@app.route("/owner/<username>/<placename>/<place_address>")
def displayqr_page(placename, username, place_address):
    if session.get("account_type") == "owner":
        return render_template(
            "displayqrcode.html", placename=placename, username=username, place_address=place_address
        )
    else:
        return redirect(url_for("login_page"))

@app.route("/timer_page/<user_name>/<place_address>/<place_name>", methods=["GET", "POST"]
)
def timer_page(user_name, place_address, place_name):
    if request.method == "POST":
        # When person clicks "leave" their exit date is saved
        exitdate = datetime.datetime.now()
        try:
            # Updating table with the exit date
            with db.cursor() as cur:
                cur.execute(
                    "UPDATE VisitorToPlaces SET ExitDateTime=%s WHERE Visitor=%s AND ExitDateTime IS NULL",
                    (exitdate, user_name),
                )
                db.commit()
                print("VisitorToPlaces updated exit time")
        finally:
            cur.close()
        return redirect(url_for("scan_page", user_name=user_name))
    else:
        if session.get("account_type") == "visitor":
            return render_template(
                "timer.html",
                placename=place_name,
                placeaddress=place_address,
                username=user_name,
            )
        else:
            return redirect(url_for("login_page"))

@app.route("/agent/<user_name>")
def agent_page(user_name):
    if session.get("account_type") == "agent":
        return render_template("agentPage.html", username=user_name)
    else:
        return redirect(url_for("login_page"))


# main hospital page(must be logged in as hospital)
@app.route("/hospital/<user_name>", methods=["GET", "POST"])
def hospital_page(user_name):
    # Getting the data of visitors from Users table and the number of rows in the table
    with db.cursor() as cur:
        rows = cur.execute(
            "Select Name,Address,PhoneNumber,Email,Infected,UserID,UserType from User U WHERE U.UserType=%s",
            ("visitor"),
        )
        allusers = cur.fetchall()
        cur.close()
    if request.method == "POST":
        # Get list of checkboxes which are ticked
        infectedusers = request.form.getlist("mycheckbox")
        with db.cursor() as cur:
            # first mark everyone as not infected
            for i in range(1, rows + 1):
                cur.execute(
                    "UPDATE User SET infected=%s WHERE UserType=%s", (0, "visitor")
                )
                db.commit()
            # not mark the checked checkboxes as infected
            for id in infectedusers:
                print(id)
                cur.execute("UPDATE User SET infected=%s WHERE UserID=%s", (1, id))
                db.commit()
            cur.close()
            # fetching the info after we update the table
            with db.cursor() as cur:
                cur.execute(
                    "Select Name,Address,PhoneNumber,Email,Infected,UserID,UserType from User U WHERE U.UserType=%s",
                    ("visitor"),
                )
                allusers = cur.fetchall()
                cur.close()
            return render_template("hospitalPage.html", users=allusers)
    else:
        # fetching all visitors from user table
        with db.cursor() as cur:
            cur.execute(
                "SELECT Name,Address,PhoneNumber,Email,Infected,UserID,UserType FROM User U WHERE U.UserType=%s",
                ("visitor"),
            )
            users = cur.fetchall()
            cur.close()
            if session.get("account_type") == "hospital":
                return render_template("hospitalPage.html", users=users)
            else:
                return redirect(url_for("login_page"))

# add a hospital to database from form (POST)/load the page (GET)
@app.route("/agent/<user_name>/addhospital", methods=["GET", "POST"])
def registerHospital(user_name):
    if request.method == "POST":
        # getting all the info for the hospital
        name = request.form["name"]
        address = request.form["address"]
        phonenumber = request.form["phonenumber"]
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        salt = bcrypt.gensalt()
        hashpass = bcrypt.hashpw(password.encode("utf-8"), salt)
        with db.cursor() as cur:
            # checking if the username is taken
            cur.execute("SELECT Username From User U WHERE U.Username=%s ", (username))
            account = cur.fetchone()
            cur.close()
            if account:
                return render_template(
                    "hospitalRegister.html", username=user_name, usernametaken=True
                )
        with db.cursor() as cur:
            # if username not taken, add the account to database
            cur.execute(
                "INSERT INTO User(Name,Address,PhoneNumber,Email,Username,Password,Usertype,DeviceID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    name,
                    address,
                    phonenumber,
                    email,
                    username,
                    hashpass,
                    "hospital",
                    "000",
                ),
            )
            db.commit()
            cur.close()
            flash(f"new hospital added")
        return render_template("hospitalRegister.html", username=user_name)
    else:
        if session.get("account_type") == "agent":
            return render_template("hospitalRegister.html", username=user_name)

        else:
            return redirect(url_for("login_page"))


# Agent page where all users are accessed
@app.route("/agent/<user_name>/allusersaccess", methods=["GET", "POST"])
def allUserAnalytics(user_name):
    if request.method == "POST":
        # Get the searchresult in order to show only searched users
        searchresult = request.form["searchbar"]
        with db.cursor() as cur:
            # if search result is empty show every user
            if searchresult == "":
                cur.execute(
                    "SELECT UserID,Name,Address,PhoneNumber,Email,Infected,UserType FROM User U WHERE U.UserType=%s OR U.UserType=%s",
                    ("visitor", "owner"),
                )
                users = cur.fetchall()
                cur.execute("SELECT name from user")
                names = cur.fetchall()
                names = [row[0] for row in names]
                cur.close()
            else:
                # else show only users matching the searchresult
                sql = 'SELECT UserID,Name,Address,PhoneNumber,Email,Infected,UserType FROM User U WHERE (U.Name LIKE %s) AND (U.UserType="owner" OR U.UserType="visitor")'
                args = ["%" + searchresult + "%"]
                cur.execute(sql, args)

                users = cur.fetchall()
                cur.execute("SELECT name from User")
                names = cur.fetchall()
                names = [row[0] for row in names]
                cur.close()

        return render_template(
            "allUserAnalytics.html", username=user_name, users=users, names=names
        )
    else:
        # Get all users in order to display them
        with db.cursor() as cur:
            cur.execute(
                "SELECT UserID,Name,Address,PhoneNumber,Email,Infected,UserType FROM User U WHERE U.UserType=%s OR U.UserType=%s",
                ("visitor", "owner"),
            )
            users = cur.fetchall()
            if session.get("account_type") == "agent":
                cur.execute("SELECT name from User")
                names = cur.fetchall()
                names = [row[0] for row in names]
                cur.close()
                return render_template(
                    "allUserAnalytics.html",
                    username=user_name,
                    users=users,
                    names=names,
                )
            else:
                return redirect(url_for("login_page"))


########################################
def visitedplaceaccessRender(user_name, visitedplaces):
    with db.cursor() as cur:
        cur.execute("SELECT Place from VisitorToPlaces")
        places = cur.fetchall()
        places = [row[0] for row in places]
        print(places)
        visitedplaces = cur.fetchall()
        cur.execute("SELECT Visitor from VisitorToPlaces")
        names = cur.fetchall()
        names = [row[0] for row in names]
        print(names)
        cur.close()
        params = [places, names]
        return params


def sqlBuilder():
    person = request.form["name"]
    entrydate = request.form["entrydate"]
    exitdate = request.form["exitdate"]
    place = request.form["place"]
    # searching the places corresponding to the info
    ok = 0
    args = []
    sql = "SELECT Visitor,Place,EntryDateTime,ExitDateTime FROM VisitorToPlaces V "
    if person != "":
        sql += "WHERE V.Visitor LIKE %s "
        ok = 1
        args.append("%" + person + "%")

    if place != "":
        args.append("%" + place + "%")
        if ok == 1:
            sql += "AND V.Place LIKE %s "
        else:
            sql += "WHERE V.Place LIKE %s "
            ok = 1

    if entrydate != "":
        args.append(entrydate)
        if ok == 1:
            sql += "AND V.EntryDateTime>=%s "
        else:
            sql += "WHERE V.EntryDateTime>=%s "
            ok = 1

    if exitdate != "":
        args.append(exitdate)
        if ok == 1:
            sql += "AND V.ExitDateTime<=%s "
        else:
            sql += "WHERE V.ExitDateTime<=%s "
            ok = 1
    if ok == 0:
        sql = "SELECT * FROM VisitorToPlaces"

    return sql, args


# Agent page where visited places are accessed


@app.route("/agent/<user_name>/visitedplacesaccess", methods=["GET", "POST"])
def allVisitedAnalytics(user_name):
    if request.method == "POST":
        # getting the search info
        with db.cursor() as cur:
            sql = sqlBuilder()[0]
            args = sqlBuilder()[1]
            print(sql)
            print(args)
            cur.execute(sql, args)
            visitedplaces = cur.fetchall()
            cur.close()
        return render_template(
            "allVisitedAnalytics.html",
            username=user_name,
            visitedplaces=visitedplaces,
            places=visitedplaceaccessRender(user_name, visitedplaces)[0],
            names=visitedplaceaccessRender(user_name, visitedplaces)[1],
        )

    else:
        # showing every visited place
        with db.cursor() as cur:
            cur.execute("SELECT * FROM VisitorToPlaces")
            visitedplaces = cur.fetchall()
            cur.close()
        if session.get("account_type") == "agent":
            visitedplaceaccessRender(user_name, visitedplaces)
            return render_template(
                "allVisitedAnalytics.html",
                username=user_name,
                visitedplaces=visitedplaces,
                places=visitedplaceaccessRender(user_name, visitedplaces)[0],
                names=visitedplaceaccessRender(user_name, visitedplaces)[1],
            )

        else:
            return redirect(url_for("login_page"))
#########################################
@app.route("/agent/<user_name>/allplacesaccess", methods=["GET", "POST"])
def allPlacesAnalytics(user_name):
    if request.method == "POST":
        # getting the searchbar result
        searchresult = request.form["searchbar"]
        with db.cursor() as cur:
            # if nothing is entered in the search bar, show every place
            if searchresult == "":
                cur.execute("SELECT * FROM places P")
                places = cur.fetchall()
                cur.close()
            else:
                # else show the places corresponding to the search

                sql = "SELECT * FROM places P WHERE (P.PlaceName LIKE %s)"
                args = ["%" + searchresult + "%"]
                cur.execute(sql, args)

                places = cur.fetchall()
                cur.execute("SELECT PlaceName from places")
                names = cur.fetchall()
                names = [row[0] for row in names]
                print(names)
                cur.close()

        return render_template(
            "allPlacesAnalytics.html", username=user_name, places=places, names=names
        )
    else:
        # show every place
        with db.cursor() as cur:
            cur.execute("SELECT * FROM Places P")
            places = cur.fetchall()
            cur.execute("SELECT PlaceName from Places")
            names = cur.fetchall()
            names = [row[0] for row in names]
            cur.close()
            if session.get("account_type") == "agent":
                return render_template(
                    "allPlacesAnalytics.html",
                    username=user_name,
                    places=places,
                    names=names,
                )
            else:
                return redirect(url_for("login_page"))
#####################################
@app.route("/agent/<user_name>/allhospitalsaccess", methods=["GET", "POST"])
def allHospitalsAnalytics(user_name):
    if request.method == "POST":
        # getting search result
        searchresult = request.form["name"]
        with db.cursor() as cur:
            # if search result is empty show every hospital
            if searchresult == "":
                cur.execute(
                    "SELECT UserID,Name,Address,PhoneNumber,Email FROM User U WHERE U.UserType=%s",
                    ("hospital"),
                )
                hospitals = cur.fetchall()
                cur.execute('SELECT Name FROM user WHERE UserType="hospital"')
                names = cur.fetchall()
                names = [row[0] for row in names]
                cur.close()
            else:
                # else show hospitals corresponding to the search

                sql = 'SELECT UserID,Name,Address,PhoneNumber,Email FROM User U WHERE U.Name LIKE %s AND (U.UserType="hospital")'
                args = ["%" + searchresult + "%"]
                cur.execute(sql, args)

                hospitals = cur.fetchall()
                cur.execute('SELECT Name FROM user WHERE UserType="hospital"')
                names = cur.fetchall()
                names = [row[0] for row in names]
                print(names)
                cur.close()
        return render_template(
            "allHospitalsAnalytics.html",
            username=user_name,
            hospitals=hospitals,
            names=names,
        )
    else:
        # showing all hospitals
        with db.cursor() as cur:
            cur.execute(
                "SELECT UserID,Name,Address,PhoneNumber,Email FROM User U WHERE U.UserType=%s",
                ("hospital"),
            )
            hospitals = cur.fetchall()
            cur.execute('SELECT Name FROM User WHERE UserType="hospital"')
            names = cur.fetchall()
            names = [row[0] for row in names]
            print(names)
            cur.close()
            if session.get("account_type") == "agent":
                return render_template(
                    "allHospitalsAnalytics.html",
                    username=user_name,
                    hospitals=hospitals,
                    names=names,
                )
            else:
                return redirect(url_for("login_page"))
#####################################
@app.route("/agent/<user_name>/trackPossibleInfect", methods=["GET", "POST"])
def trackPossibleInfect(user_name):
    if request.method == "POST":
        searchresult = request.form["searchbar"]
        with db.cursor() as cur:
            # if search result is empty show every user
            if searchresult == "":
                cur.execute(
                    "SELECT UserID,Name,Address,PhoneNumber,Email,Infected,UserType FROM User U WHERE U.UserType=%s",
                    ("visitor"),
                )
                users = cur.fetchall()
                cur.execute('SELECT Name FROM User WHERE UserType="visitor"')
                names = cur.fetchall()
                names = [row[0] for row in names]
                cur.close()
            else:
                # else show only users matching the searchresult
                sql = 'SELECT UserID,Name,Address,PhoneNumber,Email,Infected,UserType FROM User U WHERE (U.Name LIKE %s) AND (U.UserType="visitor")'
                args = ["%" + searchresult + "%"]
                cur.execute(sql, args)

                users = cur.fetchall()
                cur.execute('SELECT Name FROM User WHERE UserType="visitor"')
                names = cur.fetchall()
                names = [row[0] for row in names]
                cur.close()

        return render_template(
            "trackPossibleInfect.html", username=user_name, users=users, names=names
        )

    else:
        if session.get("account_type") == "agent":
            with db.cursor() as cur:
                cur.execute(
                    "SELECT UserID,Name,Address,PhoneNumber,Email,Infected,UserType FROM User U WHERE U.UserType=%s",
                    ("visitor"),
                )
                users = cur.fetchall()
                cur.execute('SELECT Name FROM User WHERE UserType="visitor"')
                names = cur.fetchall()
                names = [row[0] for row in names]
                cur.close()
                print(names)

            return render_template(
                "trackPossibleInfect.html", username=user_name, names=names, users=users
            )

        else:
            return redirect(url_for("login_page"))
##############################
@app.route("/agent/<user_name>/trackPossibleInfect/<user>", methods=["GET", "POST"])
def trackEachInfect(user_name, user):
    if session.get("account_type") == "agent":
        return render_template("trackEachInfect.html", username=user_name, user=user)
    else:
        return redirect(url_for("login_page"))


# this route is not used. 
@app.route("/markVisitor", methods=["POST"])
def markVisitor():
    if session.get("account_type") == "hospital":
        user_id = request.form["user_id"]
        status = request.form["status"]
        cursor = db.cursor()
        cursor.execute(
            "UPDATE user U SET U.infected=%s WHERE U.user_id=%s", (status, user_id)
        )
        # It wont do anything without db.commit()
        db.commit()
        return {"ok": True, "new_status": status}
    else:
        return redirect(url_for("loginHospital"))


# updates the hospital status
# from the ajax POST request (see hospitalAction.js)
@app.route("/hospitalAction", methods=["POST"])
def hospitalAction():
    if session.get("account_type") == "agent":
        hospital_id = request.form["hospitalId"]
        status = request.form["status"]
        cursor = db.cursor()
        cursor.execute(
            "UPDATE hospital H SET H.status=%s WHERE H.hospital_id=%s",
            (status, hospital_id),
        )
        # It wont do anything without db.commit()
        db.commit()
        return {"ok": True, "new_status": status}
    else:
        return redirect(url_for("loginAgent"))


@app.errorhandler(404)
def notFound_error(e):
    return render_template("404.html")



#########################################################

""" @CHANGE

    This code allows the server to be started by simply
    running this python file with the following command
    in this directory:

    $ python server.py

    If there are issues, try changing the port
"""

# close session on logout request
@app.route("/logout")
def logout():
    session.pop("username", None)
    session.clear()
    return redirect(url_for("login_page"))

if __name__ == "__main__":
    app.run(debug=True)


#########################################################
