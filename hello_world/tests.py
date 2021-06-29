from unittest import TestCase
from app import lambda_handler

class Test(TestCase):
    def test_no_path_parameters(self):
        api_gateway_event_stub = {} # empty because expecting empty test parameters
        expected = "invalid_request_response"
        actual = lambda_handler(api_gateway_event_stub, None)

        self.assertEqual(
            actual, 
            expected, 
            msg='Did not get invalid response when path parameters was empty'
        )