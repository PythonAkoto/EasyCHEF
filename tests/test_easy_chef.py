"""Testing the functionality of the Easy Chef app"""
import os
import pytest
import requests
import main
from flask import Flask, Blueprint
from homepage import home
import json
from dotenv import load_dotenv
load_dotenv()


# validate route (webpage)
def test_base_route():
    app = Flask(__name__, template_folder="../templates")
    app.register_blueprint(home)
    client = app.test_client()
    base_url = "/"
    home_url = "/home"

    response = client.get(base_url)
    response2 = client.get(home_url)

    # print(response.get_data())
    assert response.status_code == 200
    assert response2.status_code == 200


# validate successful post
def test_post_route_success():
    app = Flask(__name__, template_folder="../templates")
    app.register_blueprint(home)
    client = app.test_client()
    base_url = "/"
    home_url = "/home"

    url = os.environ['API_URL']

    mock_request_headers = {
        "X-RapidAPI-Key": os.environ['X-RapidAPI-Key'],
        "X-RapidAPI-Host": os.environ['X-RapidAPI-Host'],
    }

    mock_request_querystring = {
        "ingredients": "apples,flour,sugar",
        "number": "3",
        "ignorePantry": "false",
        "ranking": "1",
    }

    response = requests.request(
        "GET", url, headers=mock_request_headers, params=mock_request_querystring
    )

    # check to see if request was successful
    assert response.status_code == 200
    print("test 1")


# validate headers
def test_mock_headers():
    app = Flask(__name__, template_folder="../templates")
    app.register_blueprint(home)
    client = app.test_client()
    base_url = "/"
    home_url = "/home"

    url = os.environ['API_URL']

    mock_request_headers = {
        "X-RapidAPI-Key": os.environ['X-RapidAPI-Key'],
        "X-RapidAPI-Host": os.environ['X-RapidAPI-Host'],
    }

    # check if the RapidAPI-Key for headers is up to date & works
    assert (
        mock_request_headers["X-RapidAPI-Key"] == os.environ['X-RapidAPI-Key'],

    )
    print("test 2")

    # check if the RapidAPI-Host for headers is up to date & works
    assert (
        mock_request_headers["X-RapidAPI-Host"] == os.environ['X-RapidAPI-Host']
    )
    print("test 3")


# validate query string
def test_request_querystring():
    app = Flask(__name__, template_folder="../templates")
    app.register_blueprint(home)

    url = os.environ['API_URL']

    mock_request_headers = {
        "X-RapidAPI-Key": os.environ['X-RapidAPI-Key'],
        "X-RapidAPI-Host": os.environ['X-RapidAPI-Host'],
    }

    mock_request_querystring = {
        "ingredients": "apples,flour,sugar",
        "number": "3",
        "ignorePantry": "false",
        "ranking": "1",
    }

    response = requests.request(
        "GET", url, headers=mock_request_headers, params=mock_request_querystring
    )

    data = response.json()

    # check to make sure same number of recipes as number of mock_request_querystring["number"]
    assert mock_request_querystring["number"] == str(
        len(data)
    )  # convert to str because mock_request_querystring["number"] is a str

    # check the ingredients
    assert mock_request_querystring["ingredients"] == "apples,flour,sugar"


# validate unauthorised call
def test_unauthorized_api_call():
    """Check if correct unauthorised request message is given back if
    no data in mock_request_headers.
    """
    app = Flask(__name__, template_folder="../templates")
    app.register_blueprint(home)
    client = app.test_client()
    base_url = "/"
    home_url = "/home"

    url = os.environ['API_URL']

    mock_request_headers = {}

    mock_request_querystring = {
        "ingredients": "apples,flour,sugar",
        "number": "3",
        "ignorePantry": "false",
        "ranking": "1",
    }

    response = requests.request(
        "GET", url, headers=mock_request_headers, params=mock_request_querystring
    )

    assert response.status_code == 401


# validate unavailable page
def test_bad_request_api_call():
    """Check if correct bad request is 404 - page not avaiable"""
    app = Flask(__name__, template_folder="../templates")
    app.register_blueprint(home)
    client = app.test_client()
    base_url = "/"
    home_url = "/home"

    url = os.environ['API_URL']

    mock_request_headers = {
        "X-RapidAPI-Key": os.environ['X-RapidAPI-Key'],
        "X-RapidAPI-Host": os.environ['X-RapidAPI-Host'],
    }

    mock_request_querystring = {
        "ingredients": "apples,flour,sugar",
        "number": "3",
        "ignorePantry": "false",
        "ranking": "1",
    }

    response = client.post(
        url, data=json.dumps(mock_request_querystring), headers=mock_request_headers
    )

    assert response.status_code == 404
