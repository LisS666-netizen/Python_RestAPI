import requests


class Base:

    def __get_request(self, url, headers):
        return requests.request('GET', url, headers=headers)

    def __post_request(self, url, headers=None, payload=None):
        return requests.request('POST', url, headers=headers, json=payload)

    def __put_request(self, url, headers=None, payload=None):
        return requests.request('PUT', url, headers=headers, json=payload)

    def __delete_request(self, url, headers=None):
        return requests.request('DELETE', url, headers=headers)

    def get_response(self, request_type, url, headers=None, payload=None):
        if request_type == 'GET':
            return self.__get_request(url, headers)
        if request_type == 'POST':
            return self.__post_request(url, headers, payload)
        if request_type == 'PUT':
            return self.__put_request(url, headers, payload)
        if request_type == 'DELETE':
            return self.__delete_request(url, headers)
