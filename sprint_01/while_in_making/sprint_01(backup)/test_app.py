import unittest
from flask import request
from corona import app
from corona.models import Visitor, Place, Hospital, Agent
from corona.forms import visitorLoginForm, placeLoginForm, agentLoginForm, hospitalLoginForm
from corona import bcrypt
from flask_login import current_user

class CoronaTestCases(unittest.TestCase):
    # The home page opens successfully
    def test_home_page(self):
        request = app.test_client(self)
        response = request.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.data)

    # the select login page opens successfully
    def test_login_selector_page(self):
        request = app.test_client(self)
        response = request.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'respective login type', response.data)

    # the visitor login page opens successfully
    def test_visitor_login_page(self):
        request = app.test_client(self)
        response = request.get('/login/visitorLogin', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Visitor LOGIN', response.data)

    # the place login page opens successfully
    def test_place_login_page(self):
        request = app.test_client(self)
        response = request.get('/login/placelogin', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Place LOGIN', response.data)
    
    # the hospital login page opens successfully
    def test_hospital_login_page(self):
        request = app.test_client(self)
        response = request.get('/login/hospitallogin', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hospital LOGIN', response.data)
    
    # the agent login page opens successfully
    def test_agent_login_page(self):
        request = app.test_client(self)
        response = request.get('/login/agentlogin', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Agent LOGIN', response.data)
    
    # the select segistration page opens successfully
    def test_register_selector_page(self):
        request = app.test_client(self)
        response = request.get('/register', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'respective registration type', response.data)
    
    # the visitor register page opens successfully
    def test_visitor_register_page(self):
        request = app.test_client(self)
        response = request.get('/register/visitorRegister', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Visitor Registration', response.data)
    
    # the place register page opens successfully
    def test_place_register_page(self):
        request = app.test_client(self)
        response = request.get('/register/placeRegister', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Place Registration', response.data)
    
    # the hospital register page opens successfully
    def test_hospital_register_page(self):
        request = app.test_client(self)
        response = request.get('/register/hospitalRegister', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hospital Registration', response.data)

    # the visitor login page works successfully
    def test_visitor_login(self):
        request = app.test_client(self)
        response = request.post('/login/visitorLogin', data=dict(username="visitor1", password="password"), follow_redirects=True)
        self.assertIn(b'Login', response.data)
        # self.assertTrue(current_user.username == "visitor1")
        self.assertTrue(response.status_code == 200)

    # the place login page works successfully
    def test_place_login(self):
        request = app.test_client(self)
        response = request.post('/login/placeLogin', data=dict(username="place1", password="password"), follow_redirects=True)
        # self.assertIn(b'Login', response.data)
        self.assertTrue(response.status_code == 200)

    # the hospital login page works successfully
    def test_hospital_login(self):
        request = app.test_client(self)
        response = request.post('/login/hospitalLogin', data=dict(username="hospital1", password="password"), follow_redirects=True)
        # self.assertIn(b'Login', response.data)
        self.assertTrue(response.status_code == 200)

    # the agent login page works successfully
    def test_agent_login(self):
        request = app.test_client(self)
        response = request.post('/login/agentLogin', data=dict(username="agent1", password="password"), follow_redirects=True)
        self.assertIn(b'hello', response.data)
        # self.assertTrue(response.status_code == 200)

    def test_visitor_register(self):
        request = app.test_client(self)
        response = request.post('/register/visitorRegister', data=dict(username="visitor1", password="password"), follow_redirects=True)
        self.assertIn(b'Visitor Registration', response.data)

    def test_place_register(self):
        request = app.test_client(self)
        response = request.post('/register/placeRegister', data=dict(username="place1", password="password"), follow_redirects=True)
        self.assertIn(b'Place Registration', response.data)

    def test_hospital_register(self):
        request = app.test_client(self)
        response = request.post('/register/hospitalRegister', data=dict(username="place1", password="password"), follow_redirects=True)
        self.assertIn(b'Hospital Registration', response.data)

    

if __name__ == '__main__':
    unittest.main()
