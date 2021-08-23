import requests
import json
from dataclasses import dataclass


@dataclass
class HttpRes:
    status_code: int
    text: str
    as_dict: object
    headers: dict
    req: dict


class HttpReq:
    """
    This class creates an HTTP Req object.
    Using this object, HTTP Request with different mehtods can be sent to server.
    This is just a test project for API Testing practice.
    """

    def __init__(self):
        self.base_url = 'http://httpbin.org/'
        self.headers = {'Accept': 'application/json'}

    def process_response(self, response):
        status_code = response.status_code
        text = response.text
        headers = response.headers
        req = response.request
        try:
            as_dict = response.json()
        except json.decoder.JSONDecodeError:
            as_dict = {}
        return HttpRes(status_code, text, as_dict, headers, req)

    def send_http_get_request(self):
        resp = requests.get(url=self.base_url+'get')
        return self.process_response(resp)

    def send_http_post_request(self):
        resp = requests.post(url=self.base_url+'post')
        return self.process_response(resp)

    def send_http_put_request(self):
        resp = requests.put(url=self.base_url+'put')
        return self.process_response(resp)

    def send_http_patch_request(self):
        resp = requests.patch(url=self.base_url+'patch')
        return self.process_response(resp)

    def send_http_delete_request(self):
        resp = requests.delete(url=self.base_url+'delete')
        return self.process_response(resp)
