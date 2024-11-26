import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from resources.status_code import StatusCode
from source.http_req import HttpReq


class TestHttpReq(unittest.TestCase):
    """
    A class that contains test methods (inherited from unittest.TestCase)
    to send HTTP Request and checks HTTP Response sent by server
    """

    def setUp(self) -> None:
        self.reqObj = HttpReq()
        self.response = None

    def tearDown(self) -> None:
        del self.response

    def test_001_http_get_request(self):
        print("This is a test file created for testing")


