import unittest
import requests
from bs4 import BeautifulSoup
from requests.structures import CaseInsensitiveDict


class CoronArchiveTestCase(unittest.TestCase):
    API_URL = "http://clabsql.clamv.jacobs-university.de/~sgiri/se-02-team-17/"

    def test_home_page(self):
        response = requests.get(self.API_URL)
        self.assertEqual(response.status_code, 200)
        # print(response.content)
        self.assertIn(
            b'The Best Web Service<br>for Corona Infections', response.content)

    def test_login_page_status_code(self):
        response = requests.get(self.API_URL+"login.php")
        # print(response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_login_page_page_content(self):
        response = requests.get(self.API_URL+"login.php")
        self.assertIn(b'Select Login Type', response.content)

    def test_login_page_visitor_status_code(self):
        response = requests.get(self.API_URL+"visitor/visitor_login.php")
        # print(response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_login_page_visitor_content(self):
        response = requests.get(self.API_URL+"visitor/visitor_login.php")
        self.assertIn(b'Visitor Login Form', response.content)

    def test_login_page_place_status_code(self):
        response = requests.get(self.API_URL+"places/places_login.php")
        # print(response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_login_page_place_content(self):
        response = requests.get(self.API_URL+"places/places_login.php")
        self.assertIn(b'Place Login Form', response.content)

    def test_login_page_agency_status_code(self):
        response = requests.get(self.API_URL+"agency/agency_login.php")
        # print(response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_login_page_agency_content(self):
        response = requests.get(self.API_URL+"agency/agency_login.php")
        self.assertIn(b'Agent Login Form', response.content)

    def test_login_page_hospital_status_code(self):
        response = requests.get(self.API_URL+"hospital/hospital_login.php")
        # print(response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_login_page_hospital_content(self):
        response = requests.get(self.API_URL+"hospital/hospital_login.php")
        self.assertIn(b'Hospital Login Form', response.content)

    def test_visitorRegistration(self):
        data = {
            "name":"First Visitor",
            "address" :"visitor1 address",
            "phone":"1234567890",
            "email" : "visitor1@gmail.com",
            "password" : "password",
        }
        response = requests.post(self.API_URL+"visitor/visitors_register.php", data=data)
        self.assertIn("Visitor Registration Form", response.text)

if __name__ == '__main__':
    unittest.main()