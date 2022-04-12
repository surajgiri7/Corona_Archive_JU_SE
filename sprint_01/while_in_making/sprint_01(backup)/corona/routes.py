from csv import register_dialect
from flask import render_template, request, url_for, flash, redirect, session
from corona.forms import hospitalLoginForm, placeLoginForm, visitorLoginForm, visitorRegistrationForm, visitorRegistrationForm
from corona.forms import placeRegistrationForm, hospitalRegistrationForm, visitorLoginForm, placeRegistrationForm, hospitalRegistrationForm, agentLoginForm
from corona import app, db, bcrypt
from corona.models import Visitor, Place, Hospital, Agent #, VisitorToPlaces
from flask_login import login_user, current_user, logout_user


# route to Home Page 
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


# route to Select Registration Page
@app.route('/register')
def selectUserType():
    return render_template('./RegistrationPages/selectUserType.html')

# route to the Visitor Registration Page
@app.route('/register/visitorRegister', methods=['GET', 'POST'])
def visitorRegister():
    # if the user is already loggen in, then
    # redirecting the user to home page
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = visitorRegistrationForm() #instance of the visitor registration
    # if the form is valid, then feeding the data into the data base
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        visitor = Visitor(username=form.username.data, 
                        password=hashed_pwd, 
                        email=form.email.data, 
                        visitor_name=form.visitor_name.data, 
                        address=form.address.data, 
                        city=form.city.data, 
                        device_id=form.device_id.data)
        db.session.add(visitor)
        db.session.commit()
        flash(f'Account Created for {form.visitor_name.data}!', 'success')
        return redirect(url_for('home'))
    else:
        # print(form.errors)
        flash(f'Something went wrong. Retry')
    return render_template('./RegistrationPages/visitorRegister.html', title='VisitorRegister', form=form)

# route to Place Registration Page
@app.route('/register/placeRegister', methods=['GET', 'POST'])
def placeRegister():
    # if the user is already loggen in, then
    # redirecting the user to home page
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = placeRegistrationForm() #instance of the visitor registration
    # if the form is valid, then feeding the data into the data base
    print("fghj")
    if form.validate_on_submit():
        # print("fghj")
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        place = Place(username=form.username.data, 
                        password=hashed_pwd, 
                        email=form.email.data, 
                        place_name=form.place_name.data, 
                        address=form.address.data, 
                        city=form.city.data) 
        db.session.add(place)
        db.session.commit()
        flash(f'Account Created for {form.place_name.data}!', 'success')
        return redirect(url_for('home'))
    else:
        print(form.errors)
        flash(f'Something went wrong. Retry')
    return render_template('./RegistrationPages/placeRegister.html', title='PlaceRegister', form=form)

# route to Hospital Registration Page
@app.route('/register/hospitalRegister', methods=['GET', 'POST'])
def hospitalRegister():
    # if the user is already loggen in, then
    # redirecting the user to home page
    if current_user.is_authenticated: 
        return redirect(url_for('home'))
    form = hospitalRegistrationForm() #instance of the visitor registration
    # if the form is valid, then feeding the data into the data base
    if form.validate_on_submit():
        print("fghj")
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        hospital = Hospital(username=form.username.data, 
                        password=hashed_pwd, 
                        email=form.email.data, 
                        hospital_name=form.hospital_name.data, 
                        address=form.address.data, 
                        city=form.city.data) 
        db.session.add(hospital)
        db.session.commit()
        flash(f'Account Created for {form.hospital_name.data}!', 'success')
        return redirect(url_for('home'))
    else:
        flash(f'Something went wrong. Retry')
    return render_template('./RegistrationPages/hospitalRegister.html', title='HospitalRegister', form=form)


# route to the Select Login Page
@app.route('/login')
def selectLoginType():
    return render_template('login.html')

# route to the Visitor Login Page
@app.route('/login/visitorLogin', methods=['GET', 'POST'])
def visitorLogin():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = visitorLoginForm()
    if form.validate_on_submit():
        print('lol')
        visitor = Visitor.query.filter_by(username=form.username.data).first()
        if visitor and bcrypt.check_password_hash(visitor.password, form.password.data):
            session["user"] = "Visitor"
            try:
                login_user(visitor, remember=form.remember.data)
                return redirect(url_for('home'))
            except Exception as e: 
                print(e)
        else:
           flash('Login Unsuccessful Please check username and password', 'danger')
    return render_template('./LoginPages/visitorLogin.html', title='VisitorLogin', form=form)

# route to the Place Login Page
@app.route('/login/placelogin', methods=['GET', 'POST'])
def placeLogin():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = placeLoginForm()
    print('l')
    if form.validate_on_submit():
        place = Place.query.filter_by(username=form.username.data).first()
        if place and bcrypt.check_password_hash(place.password, form.password.data):
            print('lll')
            session["user"] = "Place"
            try:
                login_user(place, remember=form.remember.data)
                print('llllll')

                return redirect(url_for('home'))
                # return redirect(url_for('afterplaceLogin'))
            except Exception as e: 
                print(e)
        else:
           flash('Login Unsuccessful Please check username and password', 'danger')
    return render_template('./LoginPages/placeLogin.html', title='PlaceLogin', form=form)




# @app.route('/placeloggedin')
# def afterplaceLogin():
#     return render_template("place_loggedin.html")

@app.route('/home/agentLoggedin')
def afterAgentLogin():
    return render_template("./afterLogin/afterAgentLogin.html")







# route to the Hospital Login Page
@app.route('/login/hospitallogin', methods=['GET', 'POST'])
def hospitalLogin():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = hospitalLoginForm()
    if form.validate_on_submit():
        print('lol')
        hospital = Hospital.query.filter_by(username=form.username.data).first()
        if hospital and bcrypt.check_password_hash(hospital.password, form.password.data):
            session["user"] = "Hospital"
            try:
                login_user(hospital, remember=form.remember.data)
                return redirect(url_for('home'))
            except Exception as e: 
                print(e)
        else:
           flash('Login Unsuccessful Please check username and password', 'danger')
    return render_template('./LoginPages/hospitalLogin.html', title='HospitalLogin', form=form)

# route to the Agent Login Page
@app.route('/login/agentlogin', methods=['GET', 'POST'])
def agentLogin():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = agentLoginForm()
    if form.validate_on_submit():
        print('lol')
        agent = Agent.query.filter_by(username=form.username.data).first()
        if agent and (agent.password, form.password.data):
            session["user"] = "Agent"
            try:
                print('lolllll')
                login_user(agent, remember=form.remember.data)
                return redirect(url_for('afterAgentLogin'))
            except Exception as e: 
                print(e)
        else:
           flash('Login Unsuccessful Please check username and password', 'danger')
    return render_template('./LoginPages/agentLogin.html', title='HospitalLogin', form=form)

# route for the logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))