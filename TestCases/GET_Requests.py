import json

import jsonpath
import requests

url = "https://reqres.in"


def test_get_all_users():
    response = requests.get(url + "/api/users?page=2")
    assert response.status_code == 200
    json_response = json.loads(response.text)
    print(json_response)
    pages = jsonpath.jsonpath(json_response, "total_pages")
    print(pages[0])
    assert pages[0] == 2


def test_get_user():
    response = requests.get(url + "/api/user/2")
    assert response.status_code == 200
    response_json = json.loads(response.text)
    # print(json_response)
    print('\n', jsonpath.jsonpath(response_json, 'data.id')[0])
    print(jsonpath.jsonpath(response_json, 'data.name')[0])


def test_user_not_found():
    response = requests.get(url + '/api/users/4')
    assert response.status_code == 404


def test_list_resources():
    """Testing"""
    response = requests.get(url + '/api/unknown')
    json_string = json.loads(response.content)
    print(json_string)
