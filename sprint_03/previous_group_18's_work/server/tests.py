# NOTE: For this file to work effectively you must first
# call the "initTables.sql" and "addData.sql" files
# in the /database folder.

# MAKE SURE YOU RUN THIS FILE FROM THIS DIRECTORY
# Run with the following command:
''' $ pytest -q tests.py '''

import sys, os
from server import create_app
import pytest

# Adds current directory to PYTHONPATH
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath)

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    # other setup can go here
    yield app
    # clean up / reset resources here

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

# THE FOLLOWING FUNCTIONS ARE THE TESTS
def test_homepage_page(client):
    response = client.get("/")
    assert b"<h2>WHICH ONE ARE YOU?</h2>" in response.data

# this should fail
def test_homepage_page(client):
    response = client.get("/")
    assert b"<h2>bla bla bla 92qjyfg85613 I don't exist!</h2>" in response.data

def test_imprint_page(client):
    response = client.get("/imprint")
    assert response.request.path == "/imprint"

def test_login_page(client):
    response = client.get("/login")
    assert response.request.path == "/login"

def test_homepage_page(client):
    response = client.get("/login")
    assert response.request.path == "/login"

def test_login_post(client):
    response = client.get("/login")
    client.post("username=test&password=test")
    # check for redirect
    assert response.request.path == "/index"

# this should fail
def test_login_post(client):
    response = client.get("/login")
    client.post("username=test&password=thisisawrongpassword")
    # check for redirect
    assert response.request.path == "/index"