from Requests.BaseClass import Base
from Requests.Properties import Properties

url = 'https://gorest.co.in'
property_obj = Properties()
base_obj = Base()

property_obj.request_type = 'GET'
property_obj.url = url + '/public-api/users'
property_obj.headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer pJpMr1MHHccRJUQo9jW4Ue7TX8uy-dVWVIBY',
    'Cookie': '_csrf=1195f7064d4bd114c7ba43c68c377719fea8ba9bd876be0d765b294c56aaaf97a%3A2%3A%7Bi%3A0%3Bs%3A5%3A'
              '%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22KtqK1QPSuI9AOfIGAp7qu161HHbxAbZD%22%3B%7D '
}


def test_list_all_users():
    """
    List all users
    :return: all users
    """
    response = base_obj.get_response(property_obj.request_type, property_obj.url, property_obj.headers)
    print('\n' + str(response.json()))
    response_json = response.json()
    assert response.status_code == 200
    assert response_json['code'] == 200
    assert response_json['meta']['pagination']['limit'] == 20


def test_list_all_users_negative():
    """
    The requested resource does not exists
    :return: 404 - Requested resource does not exists
    """
    property_obj.request_type = 'GET'
    property_obj.url = url + '/public-api/user'
    response = base_obj.get_response(property_obj.request_type, property_obj.url, headers=property_obj.headers)
    assert response == 404


def test_list_all_users_with_invalid_authentication():
    headers = {
        'Content-Type': 'application/json'
    }

    response = base_obj.get_response(property_obj.request_type, property_obj.url, headers=headers)
    print(response.content)
