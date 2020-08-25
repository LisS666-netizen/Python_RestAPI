class Properties:

    def __init__(self, request_type=None, url=None, headers=None, payload=None):
        self.__request_type = request_type
        self.__url = url
        self.__headers = headers
        self.__payload = payload

    @property
    def request_type(self):
        return self.__request_type

    @request_type.setter
    def request_type(self, request_type):
        self.__request_type = request_type

    @property
    def headers(self):
        return self.__headers

    @headers.setter
    def headers(self, headers):
        self.__headers = headers

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        self.__url = url

    @property
    def payload(self):
        return self.__payload

    @payload.setter
    def payload(self, payload):
        self.__payload = payload


