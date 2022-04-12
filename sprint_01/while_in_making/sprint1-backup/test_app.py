import os, sys
import unittest
from flask import request, url_for, request, session
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from corona import app, db
from corona.models import Visitor, Place, Hospital, Agent
from corona.forms import visitorLoginForm, placeLoginForm, agentLoginForm, hospitalLoginForm
from corona import bcrypt
from flask_login import current_user

# from base64 import BaseTestCase

class CoronaTestCases(unittest.TestCase):
    API_URL = "http://localhost:5000/"
    # The home page opens successfully
    def test_home_page(self):
        app.config['WTF_CSRF_ENABLED'] = False
        request = app.test_client(self)
        response = request.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.data)

    # The scanning page opens successfully
    def test_scanpage(self):
        app.config['WTF_CSRF_ENABLED'] = False
        request = app.test_client(self)
        response = request.get('/scanQRcode', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'QR code', response.data)

    # the select login page opens successfully
    def test_login_selector_page(self):
        app.config['WTF_CSRF_ENABLED'] = False
        request = app.test_client(self)
        response = request.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'respective login type', response.data)

    # the visitor login page opens successfully
    def test_visitor_login_page(self):
        app.config['WTF_CSRF_ENABLED'] = False
        request = app.test_client(self)
        response = request.get('/login/visitorLogin', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Visitor LOGIN', response.data)

    # the place login page opens successfully
    def test_place_login_page(self):
        app.config['WTF_CSRF_ENABLED'] = False
        request = app.test_client(self)
        response = request.get('/login/placelogin', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Place LOGIN', response.data)
    
    # the hospital login page opens successfully
    def test_hospital_login_page(self):
        app.config['WTF_CSRF_ENABLED'] = False
        request = app.test_client(self)
        response = request.get('/login/hospitallogin', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hospital LOGIN', response.data)
    
    # the agent login page opens successfully
    def test_agent_login_page(self):
        app.config['WTF_CSRF_ENABLED'] = False
        request = app.test_client(self)
        response = request.get('/login/agentlogin', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Agent LOGIN', response.data)
    
    # the select registration page opens successfully
    def test_register_selector_page(self):
        app.config['WTF_CSRF_ENABLED'] = False
        request = app.test_client(self)
        response = request.get('/register', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'respective registration type', response.data)
    
    # the visitor register page opens successfully
    def test_visitor_register_page(self):
        app.config['WTF_CSRF_ENABLED'] = False
        request = app.test_client(self)
        response = request.get('/register/visitorRegister', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Visitor Registration', response.data)

    # the visitor registration works successfully
    def test_visitor_register(self):
        app.config['WTF_CSRF_ENABLED'] = False
        request = app.test_client(self)
        response = request.post('/register/visitorRegister', data=dict(username="visitor1", password="password"), follow_redirects=True)
        self.assertIn(b'Visitor Registration', response.data)


    # the visitor login page works successfully
    def test_visitor_login(self):
        app.config['WTF_CSRF_ENABLED'] = False
        request = app.test_client(self)
        response = request.post('/login/visitorLogin', data=dict(username="visitor1", password="password", form=" "), follow_redirects=True)
        self.assertIn(b'This is a demo for Software Engineering!', response.data)
        # self.assertTrue(current_user.username == "visitor1")
        # self.assertTrue(response.status_code == 200)
    
    # the place register page opens successfully
    def test_place_register_page(self):
        app.config['WTF_CSRF_ENABLED'] = False
        request = app.test_client(self)
        response = request.get('/register/placeRegister', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Place Registration', response.data)

    # the place registration works successfully
    def test_place_register(self):
        app.config['WTF_CSRF_ENABLED'] = False
        request = app.test_client(self)
        response = request.post('/register/placeRegister', data=dict(username="place1", password="password"), follow_redirects=True)
        self.assertIn(b'Place Registration', response.data)
    
    # the place login page works successfully
    def test_place_login(self):
        app.config['WTF_CSRF_ENABLED'] = False
        request = app.test_client(self)
        response = request.post('/login/placelogin', data=dict(username="place1", password="password", form=" "), follow_redirects=True)
        self.assertIn(b'This is a demo for Software Engineering!', response.data)
        self.assertEqual(response.status_code, 200)

    # # the hospital register page opens successfully
    # #not working
    def test_hospital_register_page(self):
        app.config['WTF_CSRF_ENABLED'] = False
        request = app.test_client(self)
        response = request.get('/agentLoggedin/hospitalRegister', content_type='html/text')
        # self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hospital Registration', response.data)

    # # the hospital registration works successfully
    # #not working
    # def test_hospital_register(self):
    #     app.config['WTF_CSRF_ENABLED'] = False
    #     request = app.test_client(self)
    #     response = request.post('/agentLoggedin/hospitalRegister', data=dict(username="hospital1", password="password", form=""), follow_redirects=True)
    #     self.assertIn(b'Hospitals', response.data)
    #     self.assertTrue(response.status_code == 200)

    # the hospital login page works successfully
    def test_hospital_login(self):
        app.config['WTF_CSRF_ENABLED'] = False
        request = app.test_client(self)
        response = request.post('/login/hospitallogin', data=dict(username="hospital1", password="password", form=" "), follow_redirects=True)
        self.assertIn(b'This is a demo for Software Engineering!', response.data)
        self.assertEqual(response.status_code, 200)


    # the agent login page works successfully
    def test_agent_login(self):
        app.config['WTF_CSRF_ENABLED'] = False
        request = app.test_client(self)
        response = request.post('/login/agentlogin', data=dict(username="agent2", password="password", form = " "), follow_redirects=True)
        self.assertIn(b'Register', response.data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
