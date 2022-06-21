from app import app
import unittest
from app import secret

class FlaskTest(unittest.TestCase):
    API_URL = "http://http://127.0.0.1:5000//"
    # The home page opens successfully

    def test_home_page(self):
        # app.config['WTF_CSRF_ENABLED'] = False
        request = app.test_client(self)
        response = request.get(self.API_URL+'/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'CORONA', response.data)


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
        self.assertIn(b'Visitor Registration', response.data)

    def test_owner_registration_page(self):
        # app.config['WTF_CSRF_ENABLED'] = False
        request = app.test_client(self)
        response = request.get(self.API_URL+'/registerowner', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Owner Registration', response.data)

   # the visitor registration works successfully
    def test_visitor_register_success(self):
        response = app.test_client(self)
        app.secret_key = secret
        #Note that after a user as already been created, this will result in a failure
        response = response.post(self.API_URL+'/registervisitor', data=dict(name="aaa",
                                                            username="aaa",
                                                            email="aaa@gmail.com",
                                                            phone="789456123789456",
                                                            address="aaa address",
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
        self.assertIn(b"Visitor Registration", response.data)
        self.assertEqual(response.status_code, 200)

    # the place owner registration works successfully
    def test_owner_register_success(self):
        response = app.test_client(self)
        app.secret_key = secret
        #Note that after a user as already been created, this will result in a failure
        response = response.post(self.API_URL+'/registerowner', data=dict(name="bbb",
                                                            username="bbb",
                                                            email="bbb@gmail.com",
                                                            phone="789456123789456",
                                                            address="bbb address",
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
        self.assertIn(b"Owner Registration", response.data)
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
        response = response.post(self.API_URL+'/login', data=dict(username="agent", psw="password"), follow_redirects=True)
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



# All the old test cases written by previous sprints are commented as follows

# class ServerTest(unittest.TestCase):

#     # Sprint 1 additions

#     # Check login page is accessable
#     def test_login(self):
#         res = requests.get("http://127.0.0.1:5000/")
#         self.assertEqual(res.status_code, 200)

#     # Check visitor registration is functional
#     def test_registration_visitor(self):
#         res = requests.post(
#             "http://127.0.0.1:5000/registervisitor",
#             data={
#                 "name": "kjfdj",
#                 "username": "jfdkf",
#                 "psw": "password",
#                 "address": "campusring",
#                 "email": "xyz@fff.com",
#                 "contact": "+87074397475845",
#             },
#         )
#         self.assertEqual(res.status_code, 200)

#     # Check owner registration is functional
#     def test_registration_owner(self):
#         res = requests.post(
#             "http://127.0.0.1:5000/registervisitor",
#             data={
#                 "name": "kjfdj",
#                 "username": "jfdkf",
#                 "psw": "password",
#                 "address": "campusring",
#                 "email": "xyz@fff.com",
#                 "contact": "+87074397475845",
#             },
#         )
#         self.assertEqual(res.status_code, 200)

#     # Check that scan page is accessable
#     def test_scan(self):
#         res = requests.post(
#             "http://127.0.0.1:5000/login", data={"username": "jdoe", "pwd": "passwd"}
#         )
#         res = requests.get("http://127.0.0.1:5000/scan/jdoe")
#         self.assertEqual(res.status_code, 200)

#     # Check that owner scan page is accessable
#     def test_scan_owner(self):
#         res = requests.get("http://127.0.0.1:5000/owner/jamesdoe")
#         self.assertEqual(res.status_code, 200)

#     def test_scan_owner_username_timer(self):
#         res = requests.get("http://127.0.0.1:5000/owner/jamesdoe/location")
#         self.assertEqual(res.status_code, 200)

#     """
#         # Sprint 2 additions (+ comments for all Sprint 1 test cases)

#     """

#     # Check bad visitor registration request
#     def test_registration_visitor_2(self):
#         res = requests.post(
#             "http://127.0.0.1:5000/registervisitor",
#             data={
#                 "name": "NULL",
#                 "username": "\nick",
#                 "psw": "nick",
#                 "address": "Nick Str 1",
#                 "email": "",
#                 "contact": "",
#             },
#         )
#         self.assertEqual(res.status_code, 200)

#     # Check bad owner registration request
#     def test_registration_owner_2(self):
#         res = requests.post(
#             "http://127.0.0.1:5000/registerowner",
#             data={
#                 "name": "\\Nicole",
#                 "username": "nicoleowner",
#                 "psw": "password",
#                 "address": "nicolestrt",
#                 "email": "",
#                 "contact": "",
#             },
#         )
#         self.assertEqual(res.status_code, 200)

#     # correct hospital login
#     def test_hospital_login(self):
#         res = requests.post(
#             "http://127.0.0.1:5000/loginAgent",
#             data={"username": "nickhospital", "pwd": "nick"},
#         )
#         self.assertEqual(res.status_code, 200)

#     # correct admin login
#     def test_agent_login(self):
#         res = requests.post(
#             "http://127.0.0.1:5000/loginAgent",
#             data={"username": "admin", "pwd": "password"},
#         )
#         self.assertEqual(res.status_code, 200)

#     # Hospital login bad credentials
#     def test_hospital_login(self):
#         res = requests.post(
#             "http://127.0.0.1:5000/loginAgent",
#             data={"username": "nickhospital", "pwd": "nasfsawessgerick"},
#         )
#         self.assertEqual(res.status_code, 200)

#     # Admin login bad credentials
#     def test_agent_login_bad(self):
#         res = requests.post(
#             "http://127.0.0.1:5000/loginAgent",
#             data={"username": "admin", "pwd": "skfgjldf"},
#         )
#         self.assertEqual(res.status_code, 200)

#     # Check hospital registration
#     def test_hospital_register(self):
#         res = requests.post(
#             "http://127.0.0.1:5000/registerHospital",
#             data={
#                 "name": "Nikki's Hospital",
#                 "address": "Nikki Street 5",
#                 "username": "nikki",
#                 "email": "nikki@hospital.com",
#                 "contact": "38496793",
#                 "psw": "nikki",
#             },
#         )
#         self.assertEqual(res.status_code, 200)

#     # Check that owners can post data after logging in
#     def test_scan_owner_username(self):
#         res = requests.post(
#             "http://127.0.0.1:5000/login",
#             data={"username": "jamesdoe", "pwd": "passwd"},
#         )
#         res = requests.post(
#             "http://127.0.0.1:5000/owner/jamesdoe",
#             data={"placename": "jacobs", "address": "taunu"},
#         )
#         self.assertEqual(res.status_code, 200)


# # Call tests on file run
# if __name__ == "__main__":
#     unittest.main()