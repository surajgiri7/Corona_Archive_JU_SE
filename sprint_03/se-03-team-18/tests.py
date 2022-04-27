from app import app
import unittest
from json.encoder import ESCAPE
import os
import sys
from tkinter import E
currentdir = os.path.dirname(os.path.realpath(__name__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from app import secret

class FlaskTest(unittest.TestCase):
    API_URL = "http://http://127.0.0.1:5000//"
    # The home page opens successfully
    def test_home_page(self):
        # app.config['WTF_CSRF_ENABLED'] = False
        request = app.test_client(self)
        response = request.get(self.API_URL+'/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'MANAGIT', response.data)


    def test_login_page(self):
        # app.config['WTF_CSRF_ENABLED'] = False
        request = app.test_client(self)
        response = request.get(self.API_URL+'/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Log In', response.data)

    def test_visitor_registration_page(self):
        # app.config['WTF_CSRF_ENABLED'] = False
        request = app.test_client(self)
        response = request.get(self.API_URL+'/registervisitor', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Visitor registration', response.data)

    def test_owner_registration_page(self):
        # app.config['WTF_CSRF_ENABLED'] = False
        request = app.test_client(self)
        response = request.get(self.API_URL+'/registerowner', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Owner registration', response.data)

    # the visitor registration works successfully
    def test_visitor_register_success(self):
        response = app.test_client(self)
        app.secret_key = secret
        #Note that after a user as already been created, this will result in a failure
        response = response.post(self.API_URL+'/registervisitor', data=dict(name="haribahadur",
                                                            username="haribahadur",
                                                            email="haribahadur@gmail.com",
                                                            phone="789456123789456",
                                                            address="haribahadur address",
                                                            psw="password", form=" "
                                                            ),follow_redirects=True)
        self.assertIn(b"Log In", response.data)
        self.assertEqual(response.status_code, 200)

    # the visitor registration fail 
    def test_visitor_register_fail1(self):
        response = app.test_client(self)
        app.secret_key = secret
        response = response.post(self.API_URL+'/registervisitor', data=dict(name="",
                                                            username="",
                                                            email="",
                                                            phone="",
                                                            address="",
                                                            psw="", form=" "
                                                            ), follow_redirects=True)
        self.assertIn(b"Visitor registration", response.data)
        self.assertEqual(response.status_code, 200)

    # the place owner registration works successfully
    def test_owner_register_success(self):
        response = app.test_client(self)
        app.secret_key = secret
        #Note that after a user as already been created, this will result in a failure
        response = response.post(self.API_URL+'/registerowner', data=dict(name="madanbahadur",
                                                            username="madanbahadur",
                                                            email="madanbahadur@gmail.com",
                                                            phone="789456123789456",
                                                            address="madanbahadur address",
                                                            psw="password", form=" "
                                                            ),follow_redirects=True)
        self.assertIn(b"Log In", response.data)
        self.assertEqual(response.status_code, 200)

    # the owner registration fail 
    def test_owner_register_fail1(self):
        response = app.test_client(self)
        app.secret_key = secret

        response = response.post(self.API_URL+'/registerowner', data=dict(name="",
                                                            username="",
                                                            email="",
                                                            phone="",
                                                            address="",
                                                            psw="", form=" "
                                                            ), follow_redirects=True)
        self.assertIn(b"Owner registration", response.data)
        self.assertEqual(response.status_code, 200)

    # testing for visitor login works successfully
    def test_visitor_login(self):
        response = app.test_client(self)
        #need this for the test to work#
        app.secret_key = secret
        response = response.post(self.API_URL+'/login', data=dict(username="visitor1", psw="password"), follow_redirects=True)
        self.assertIn(b"logged in", response.data)
        self.assertEqual(response.status_code, 200)

    # testing for place owner login works successfully
    def test_owner_login(self):
        response = app.test_client(self)
        #need this for the test to work#
        app.secret_key = secret
        response = response.post(self.API_URL+'/login', data=dict(username="place1", psw="password"), follow_redirects=True)
        self.assertIn(b"Add a place", response.data)
        self.assertEqual(response.status_code, 200)

    # testing for hospital login works successfully
    def test_hospital_login(self):
        response = app.test_client(self)
        #need this for the test to work#
        app.secret_key = secret
        response = response.post(self.API_URL+'/login', data=dict(username="hospital1", psw="password"), follow_redirects=True)
        self.assertIn(b"The List of", response.data)
        self.assertEqual(response.status_code, 200)

    # testing for agent login works successfully
    def test_agent_login(self):
        response = app.test_client(self)
        #need this for the test to work#
        app.secret_key = secret
        response = response.post(self.API_URL+'/login', data=dict(username="aa", psw="aa"), follow_redirects=True)
        self.assertIn(b"Select:", response.data)
        self.assertEqual(response.status_code, 200)

    # Login Failure 
    def test_login_fail(self):
        response = app.test_client(self)
        #need this for the test to work#
        app.secret_key = secret
        response = response.post(self.API_URL+'/login', data=dict(username="bottle", psw="b"), follow_redirects=True)
        # Because it goes back to the same page
        self.assertIn(b"Log In", response.data)
        self.assertEqual(response.status_code, 200)

# testing if hospital login works successfully
    def test_agent_adding_hospital(self):
            """
            test if adding a hospital with an agent account works
            """
            with app.test_client() as tester:
                with tester.session_transaction() as session:
                    session['logged_in'] = True
                    session['agent_type'] = 'agent'
                    session['id'] = 1
                data = {
                    'name': 'random name',
                    'address': 'random@name',
                    'phonenumber': '1234512345',
                    'email': 'random@name',
                    'username': 'randomuser',
                    'password': 'password'
                }
                response = tester.post(
                    self.API_URL+'/agent/<user_name>/addhospital', data=data, follow_redirects=True)
                self.assertIn(b'Add hospital', response.data)

    # #TESTING LOG IN WITH WRONG CREDENTIALS FOR VISITOR,PLACE OWNER,HOSPITAL AND AGENT
    def test_visitor_wronglogin(self):
        response=app.test_client(self)
        response=response.get(self.API_URL+'/login',data=dict(username="wrong",password="wrong"),follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Log In',response.data)
       
    def test_owner_wronglogin(self):
        response=app.test_client(self)
        response=response.get(self.API_URL+'/login',data=dict(username="wrong",password="wrong"),follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Log In',response.data)

    def test_hospital_wronglogin(self):
        response=app.test_client(self)
        response=response.get(self.API_URL+'/login',data=dict(username="wrong",password="wrong"),follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Log In',response.data)

    def test_agent_wronglogin(self):
        response=app.test_client(self)
        response=response.get(self.API_URL+'/login',data=dict(username="wrong",password="wrong"),follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Log In',response.data)



if __name__ =="__main__":
    unittest.main()
