
from flask import Flask, render_template, request, redirect, url_for, session, flash
import datetime
import bcrypt
import pymysql
import os

# PLEASE WRITE YOUR OWN PASSWORD
db = pymysql.connect(
    host="localhost", user="root", password="@Nothing7", database="group18"
)

app = Flask(__name__)
# app.secret_key = os.urandom(32)
secret = app.secret_key = os.urandom(32)
app.secret_key = secret


# HOME
@app.route("/", methods=["GET", "POST"])
@app.route("/home")
def home():
    if session.get("account_type") == "visitor":
        return redirect(url_for("scan_page", user_name=session["account_type"]))
    elif session.get("account_type") == "owner":
        return redirect(url_for("owner_page", user_name=session["account_type"]))
    elif session.get("account_type") == "hospital":
        return redirect(url_for("hospital_page", user_name=session["account_type"]))
    elif session.get("account_type") == "agent":
        return redirect(url_for("agent_page", user_name=session["account_type"]))
    else:
        return render_template("index.html")


# imprint
@app.route("/imprint")
def imprint():
    return render_template("imprint.html")


# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login_page():
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


# REGISTRATION
@app.route("/registervisitor", methods=["GET", "POST"])
def register_visitor():
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
        infected = -1
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
        infected = -1
        # CHECKING IF USERNAME IS ALREADY TAKEN
        with db.cursor() as cur:
            cur.execute("SELECT * FROM User U WHERE U.username=%s", username)
            compare = cur.fetchone()
            cur.close()
            # IF USERNAME IS TAKEN RETURN ERROR
            if compare:
                return render_template(
                    "Placeowner_Registration.html", usernametaken=True
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
        return render_template("Placeowner_Registration.html")


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


# OWNER PAGE (PLACE REGISTRATION)
@app.route("/owner_page/<user_name>", methods=["GET", "POST"])
def owner_page(user_name):
    if request.method == "POST":
        # Getting place info
        placename = request.form["placename"]
        address = request.form["address"]
        qrcode = placename + "/" + address
        with db.cursor() as cur:
            cur.execute(
                "SELECT * FROM Places P WHERE P.PlaceName=%s AND P.PlaceAddress=%s",
                (placename, address),
            )
            place = cur.fetchone()
            cur.close()
            # checking if place exists in order not to add it twice in the database
            if place:
                return redirect(
                    url_for(
                        "displayqr_page",
                        placename=placename,
                        username=user_name,
                        place_address=address,
                    )
                )
        try:
            # Inserting info in the database
            with db.cursor() as cur:
                cur.execute(
                    "INSERT INTO Places(PlaceName,PlaceAddress,QRcode) VALUES (%s,%s,%s)",
                    (placename, address, qrcode),
                )
                db.commit()
            print("New place added")
        finally:
            cur.close()
        return redirect(
            url_for(
                "displayqr_page",
                placename=placename,
                username=user_name,
                place_address=address,
            )
        )
    else:
        if session.get("account_type") == "owner":
            return render_template("owner_page.html", Username=user_name)
        else:
            return redirect(url_for("login_page"))


# This page displays the qrcode of the place entered by place owners
@app.route("/owner_page/<username>/<placename>/<place_address>")
def displayqr_page(username, place_address, placename):
    if session.get("account_type") == "owner":
        return render_template(
            "displayqrcode.html",
            placename=placename,
            username=username,
            place_address=place_address,
        )
    else:
        return redirect(url_for("login_page"))


# Timer page
@app.route(
    "/timer_page/<user_name>/<place_address>/<place_name>", methods=["GET", "POST"]
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


# Hospital page
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
            return render_template("hospital_page.html", users=allusers)
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
                return render_template("hospital_page.html", users=users)
            else:
                return redirect(url_for("login_page"))


# Agent page (in this page there are links directing to other pages for agents)
@app.route("/agent/<user_name>")
def agent_page(user_name):
    if session.get("account_type") == "agent":
        return render_template("agent_page.html", Username=user_name)
    else:
        return redirect(url_for("login_page"))


# Agent page where all users are accessed
@app.route("/agent/<user_name>/allusersaccess", methods=["GET", "POST"])
def allusersaccess_page(user_name):
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
                cur.execute("SELECT name from user")
                names = cur.fetchall()
                names = [row[0] for row in names]
                cur.close()

        return render_template(
            "allusersaccess_page.html", username=user_name, users=users, names=names
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
                    "allusersaccess_page.html",
                    username=user_name,
                    users=users,
                    names=names,
                )
            else:
                return redirect(url_for("login_page"))


# Agent page where he can access all places
@app.route("/agent/<user_name>/allplacesaccess", methods=["GET", "POST"])
def allplacesaccess_page(user_name):
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
            "allplacesaccess_page.html", username=user_name, places=places, names=names
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
                    "allplacesaccess_page.html",
                    username=user_name,
                    places=places,
                    names=names,
                )
            else:
                return redirect(url_for("login_page"))


# Agent page where hospitals are accessed
@app.route("/agent/<user_name>/allhospitalsaccess", methods=["GET", "POST"])
def allhospitalsaccess_page(user_name):
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
            "allhospitalsaccess_page.html",
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
                    "allhospitalsaccess_page.html",
                    username=user_name,
                    hospitals=hospitals,
                    names=names,
                )
            else:
                return redirect(url_for("login_page"))


# Agent page where a hospital can be added
@app.route("/agent/<user_name>/addhospital", methods=["GET", "POST"])
def addhospital_page(user_name):
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
                    "addhospital_page.html", username=user_name, usernametaken=True
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
        return render_template("addhospital_page.html", username=user_name)
    else:
        if session.get("account_type") == "agent":
            return render_template("addhospital_page.html", username=user_name)

        else:
            return redirect(url_for("login_page"))


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
def visitedplacesaccess_page(user_name):
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
            "visitedplacesaccess_page.html",
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
                "visitedplacesaccess_page.html",
                username=user_name,
                visitedplaces=visitedplaces,
                places=visitedplaceaccessRender(user_name, visitedplaces)[0],
                names=visitedplaceaccessRender(user_name, visitedplaces)[1],
            )

        else:
            return redirect(url_for("login_page"))


@app.route("/agent/<user_name>/trackInfection", methods=["GET", "POST"])
def trackInfection(user_name):
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
            "trackInfection.html", username=user_name, users=users, names=names
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
                "trackInfection.html", username=user_name, names=names, users=users
            )

        else:
            return redirect(url_for("login_page"))


@app.route("/agent/<user_name>/trackInfection/<user>", methods=["GET", "POST"])
def trackInfectionUser(user_name, user):
    if session.get("account_type") == "agent":

        return render_template("trackInfectionUser.html", username=user_name, user=user)
    else:
        return redirect(url_for("login_page"))


# close session on logout request
@app.route("/logout")
def logout():
    session.pop("user_type", None)
    session.clear()
    return redirect(url_for("login_page"))


@app.errorhandler(404)
def notFound_error(e):
    return render_template("404.html")


if __name__ == "__main__":
    # Inside of host, please put your IPv4
    # app.run(host="134.102.121.112", debug=True, ssl_context='adhoc')
    app.run(debug=True, port=5001)
