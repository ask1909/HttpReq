import requests


class HttpReq:
    """
    This class creates an HTTP Req object.
    Using this object, HTTP Request with different mehtods can be sent to server.
    This is just a test project for API Testing practice.
    """

    def __init__(self):
        self.base_url = 'http://httpbin.org/'
        self.headers = {'Accept': 'application/json'}

    def send_http_get_request(self):
        return requests.get(url=self.base_url+'get')