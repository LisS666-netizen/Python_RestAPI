import json

import jsonpath
import requests

url = "https://reqres.in"


def test_create_new_user():
    file = open('C:\\Work\\Python_Projects\\Sample_Json\\CreateNewUser.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)
    response = requests.post(url + "/api/users", request_json)
    print(response.text)
    # Validate response code
    assert response.status_code == 201
    # Validate headers
    print(response.headers.get('Content-Type'))
    # Parse response to JSON format
    response_json = json.loads(response.text)
    print(response_json)
    print(jsonpath.jsonpath(response_json, 'id')[0])