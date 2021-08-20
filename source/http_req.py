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

    def send_http_post_request(self):
        return requests.post(url=self.base_url+'post')

    def send_http_put_request(self):
        return requests.put(url=self.base_url+'put')

    def send_http_patch_request(self):
        return requests.patch(url=self.base_url+'patch')

    def send_http_delete_request(self):
        return requests.delete(url=self.base_url+'delete')
