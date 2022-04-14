import unittest
from unittest.mock import patch, Mock

from oop.workshop.requests_handler import RequestsHandler


def mock_response(*args, **kwargs):
    class MockResponse:
        def __init__(self, *args, **kwargs):
            self.json = lambda: []
            self.status_code = 200
            self.raise_for_status = lambda: True
    return MockResponse()


class Response:
    def __init__(self, *args, **kwargs):
        self.json = lambda: []
        self.status_code = 200
        self.raise_for_status = lambda: True


def mock_response_version_two(*args, **kwargs):
    # Not working at this moment
    return Mock(return_value=Response())


@patch("requests.get", side_effect=mock_response)
class RequestsHandlerTests(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.requests_handler = RequestsHandler()

    def test_get_files(self, _):
        """ Test files list is successfully received. """
        self.assertEqual(self.requests_handler.get_files(), [])
