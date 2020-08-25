import requests


def test_rest_api_send_sms():
    headers = {
        'Host': 'rest.nexmo.com',
        'Content-Length': '45'
    }

    payload = {
        "api_key": "1fd39764",
        "api_secret": "SPDowVyrK37FGLCd",
        "from": "Vonage APIs",
        "to": "+447469336089",
        "text": "Hello from Vonage SMS API"
    }
    response_data = requests.request('POST', 'https://rest.nexmo.com/sms/json', headers=headers, json=payload).json()
    print(response_data)
    if response_data["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {response_data['messages'][0]['error-text']}")


def test_rest_api_send_sms_with_incorrect_key():
    headers = {
        'Host': 'rest.nexmo.com',
        'Content-Length': '45'
    }

    payload = {
        "api_key": "1fd3974",
        "api_secret": "SPDowVyrK37FGLCd",
        "from": "Vonage APIs",
        "to": "+447469336089",
        "text": "Hello from Vonage SMS API"
    }
    response_data = requests.request('POST', 'https://rest.nexmo.com/sms/json', headers=headers, json=payload).json()
    print(response_data)
    assert response_data['messages'][0]['status'] == '4'
    assert response_data['messages'][0]['error-text'] == 'Bad Credentials'


def test_without_client_authentication():
    headers = {
        'Host': 'rest.nexmo.com',
        'Content-Length': '45'
    }

    payload = {
        "from": "Vonage APIs",
        "to": "+447469336089",
        "text": "Hello from Vonage SMS API"
    }
    response_data = requests.request('POST', 'https://rest.nexmo.com/sms/json', headers=headers, json=payload).json()
    print(response_data)
    assert response_data['messages'][0]['status'] == '2'
    assert response_data['messages'][0]['error-text'] == 'Missing api_key'
