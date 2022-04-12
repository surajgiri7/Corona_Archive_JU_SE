from app import app
import unittest

class FlaskTest(unittest.TestCase):
    # Login page opens successfully
    def test_login(self):
        tester=app.test_client(self)
        response=tester.get("/",content_type="html/text")
        statuscode=response.status_code
        self.assertIn(b'Log In',response.data)
    #TESTING LOG IN FOR VISITOR, PLACE OWNER, HOSPITAL AND AGENT
    def test_visitor_login(self):
        tester=app.test_client(self)
        response=tester.get('/login',data=dict(username="vv",password="vv"),follow_redirects=True)
        self.assertIn(b'ab',response.data)

    def test_owner_login(self):
        tester=app.test_client(self)
        response=tester.get('/login',data=dict(username="pp",password="pp"),follow_redirects=True)
        self.assertIn(b'ab',response.data)

    def test_hospital_login(self):
        tester=app.test_client(self)
        response=tester.get('/login',data=dict(username="hh",password="hh"),follow_redirects=True)
        self.assertIn(b'ab',response.data)

    def test_agent_login(self):
        tester=app.test_client(self)
        response=tester.get('/login',data=dict(username="aa",password="aa"),follow_redirects=True)
        self.assertIn(b'ab',response.data)

    #TESTING LOG IN WITH WRONG CREDENTIALS FOR VISITOR,PLACE OWNER,HOSPITAL AND AGENT
    def test_visitor_wronglogin(self):
        tester=app.test_client(self)
        response=tester.get('/login',data=dict(username="wrong",password="wrong"),follow_redirects=True)
        self.assertIn(b'ab',response.data)

    def test_owner_wronglogin(self):
        tester=app.test_client(self)
        response=tester.get('/login',data=dict(username="wrong",password="wrong"),follow_redirects=True)
        self.assertIn(b'ab',response.data)

    def test_hospital_wronglogin(self):
        tester=app.test_client(self)
        response=tester.get('/login',data=dict(username="wrong",password="wrong"),follow_redirects=True)
        self.assertIn(b'ab',response.data)

    def test_agent_wronglogin(self):
        tester=app.test_client(self)
        response=tester.get('/login',data=dict(username="wrong",password="wrong"),follow_redirects=True)
        self.assertIn(b'ab',response.data)

if __name__ =="__main__":
    unittest.main()
