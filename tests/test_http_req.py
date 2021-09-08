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

    def test_01_http_get_request(self):
        self.response = self.reqObj.send_http_request(self.reqObj.test_data['GET'])
        self.assertEqual(self.response.status_code, StatusCode.SUCCESS, 'Should be {}'.format(StatusCode.SUCCESS))
        self.assertEqual(self.response.headers['content-type'], 'application/json', 'Should be {}'.format('application/json'))
        self.assertGreater(int(self.response.headers['content-length']), 0, 'Should be greater than {}'.format('0'))
        self.assertEqual(self.response.as_dict['headers']['User-Agent'], 'python-requests/2.26.0', 'Should be {}'.format('python-requests/2.26.0'))
        self.assertEqual(self.response.as_dict['url'], self.response.req.url)

    def test_02_http_post_request(self):
        self.response = self.reqObj.send_http_request(self.reqObj.test_data['POST'])
        self.assertEqual(self.response.status_code, StatusCode.SUCCESS, 'Should be {}'.format(StatusCode.SUCCESS))
        self.assertEqual(self.response.headers['content-type'], 'application/json', 'Should be {}'.format('application/json'))
        self.assertGreater(int(self.response.headers['content-length']), 0, 'Should be greater than {}'.format('0'))
        self.assertEqual(self.response.as_dict['headers']['User-Agent'], 'python-requests/2.26.0', 'Should be {}'.format('python-requests/2.26.0'))
        self.assertEqual(self.response.as_dict['url'], self.response.req.url)

    def test_03_http_put_request(self):
        self.response = self.reqObj.send_http_request(self.reqObj.test_data['PUT'])
        self.assertEqual(self.response.status_code, StatusCode.SUCCESS, 'Should be {}'.format(StatusCode.SUCCESS))
        self.assertEqual(self.response.headers['content-type'], 'application/json', 'Should be {}'.format('application/json'))
        self.assertGreater(int(self.response.headers['content-length']), 0, 'Should be greater than {}'.format('0'))
        self.assertEqual(self.response.as_dict['headers']['User-Agent'], 'python-requests/2.26.0', 'Should be {}'.format('python-requests/2.26.0'))
        self.assertEqual(self.response.as_dict['url'], self.response.req.url)

    def test_04_http_patch_request(self):
        self.response = self.reqObj.send_http_request(self.reqObj.test_data['PATCH'])
        self.assertEqual(self.response.status_code, StatusCode.SUCCESS, 'Should be {}'.format(StatusCode.SUCCESS))
        self.assertEqual(self.response.headers['content-type'], 'application/json', 'Should be {}'.format('application/json'))
        self.assertGreater(int(self.response.headers['content-length']), 0, 'Should be greater than {}'.format('0'))
        self.assertEqual(self.response.as_dict['headers']['User-Agent'], 'python-requests/2.26.0', 'Should be {}'.format('python-requests/2.26.0'))
        self.assertEqual(self.response.as_dict['url'], self.response.req.url)

    def test_05_http_delete_request(self):
        self.response = self.reqObj.send_http_request(self.reqObj.test_data['DELETE'])
        self.assertEqual(self.response.status_code, StatusCode.SUCCESS, 'Should be {}'.format(StatusCode.SUCCESS))
        self.assertEqual(self.response.headers['content-type'], 'application/json', 'Should be {}'.format('application/json'))
        self.assertGreater(int(self.response.headers['content-length']), 0, 'Should be greater than {}'.format('0'))
        self.assertEqual(self.response.as_dict['headers']['User-Agent'], 'python-requests/2.26.0', 'Should be {}'.format('python-requests/2.26.0'))
        self.assertEqual(self.response.as_dict['url'], self.response.req.url)
