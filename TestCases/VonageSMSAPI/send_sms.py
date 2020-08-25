import nexmo

# client = nexmo.Client()
client = nexmo.Client(key='1fd39764', secret='SPDowVyrK37FGLCd')


def test_send_sms():
    response_data = client.send_message({
        'from': 'Vonage APIs',
        'to': '+447469336089',
        'text': 'Hello from Vonage SMS API',
    })
    print(response_data)
    if response_data["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {response_data['messages'][0]['error-text']}")


def test_incorrect_client_key():
    """
    Passing wrong Client Key
    :return:
    """
    response_data = client.send_message({
        'from': 'Vonage APIs',
        'to': '07469336089',
        'text': 'Hello from Vonage SMS API',
    })
    print(response_data)
    assert response_data['messages'][0]['status'] == '4'
    assert response_data['messages'][0]['error-text'] == 'Bad Credentials'


def test_without_client_authentication():
    """
    Authentication check by passing no API_Key and API_Secret
    :return:Missing api_key, Status = 2
    Observation -> should return missing API_Key and API_Secret
    """
    response_data = client.send_message({
        'from': 'Vonage APIs',
        'to': '07469336089',
        'text': 'Hello from Vonage SMS API',
    })
    print(response_data)
    assert response_data['messages'][0]['status'] == '2'
    assert response_data['messages'][0]['error-text'] == 'Missing api_key'


def test_send_sms_to_non_listed_destination():
    """Test Non-Listed Destination
    :param - 07469336089
    :param - 7469336089
    :return Status Code -> 29; Message -> Message failed with error: Non White-listed Destination - rejected
    Observations: 1 -> should call out what are non-listed destinations and what it mean?
    """
    response_data = client.send_message({
        'from': 'Vonage APIs',
        'to': '07469336089',
        'text': 'Hello from Vonage SMS API',
    })
    assert response_data["messages"][0]["status"] == "29"
    if response_data["messages"][0]["status"] == "29":
        print(f"Message failed with error: {response_data['messages'][0]['error-text']}")
    else:
        print("Message sent successfully.")


def test_send_sms_without_from():
    """
    Observation: must return missing element from request body.
    Actual: Returning Missing from param
    :return:
    """
    response_data = client.send_message({
        'to': '447469336089',
        'text': 'Hello from Vonage SMS API'
    })
    print(response_data)
    assert response_data["messages"][0]['error-text'] == "Missing from param"
    assert response_data["messages"][0]['status'] == '2'


def test_send_sms_without_to():
    """
    Observation: must return missing element from request body.
    Actual: Returning Missing from param
    :return:
    """
    response_data = client.send_message({
        'from': 'Vonage APIs',
        'text': 'Hello from Vonage SMS API'
    })
    print(response_data)
    assert response_data["messages"][0]['error-text'] == "Missing from param"
    assert response_data["messages"][0]['status'] == '2'


def test_send_sms_without_element_text():
    """
    :return:Returning Missing Message Text
    """
    response_data = client.send_message({
        'from': 'Vonage APIs',
        'to': '447469336089',
    })
    print(response_data)
    assert response_data["messages"][0]['error-text'] == "Missing Message Text"
    assert response_data["messages"][0]['status'] == '2'


def test_send_sms_without_text():
    """
    :return:Returning Missing Message Text
    """
    response_data = client.send_message({
        'from': 'Vonage APIs',
        'to': '447469336089',
        'text': ''
    })
    print(response_data)
    assert response_data["messages"][0]['error-text'] == "Missing Message Text"
    assert response_data["messages"][0]['status'] == '2'

