import json
from unittest.mock import patch, MagicMock

import httpretty
import pytest

from buffpy.api import API
from buffpy.exceptions import BuffpyRestException


MOCKED_RESPONSE = MagicMock(content=json.dumps({"status": "ok"}))


def test_api_get_request():
    """ Should call Buffer for a given GET request. """

    mocked_session = MagicMock()
    mocked_session.get.return_value = MOCKED_RESPONSE

    with patch("buffpy.api.OAuth2Session", return_value=mocked_session):
        API(client_id="1", client_secret="2", access_token="access_token").get(url="hey")

    mocked_session.get.assert_called_once_with(url="https://api.bufferapp.com/1/hey")


def test_api_get_request_no_access_token():
    """ Should raise ValueError if the API is called without an access_token. """

    with patch("buffpy.api.OAuth2Session",
               return_value=MagicMock(access_token=None)), \
            pytest.raises(ValueError):

        API(client_id="1", client_secret="2").get(url="hey")


def test_api_post_request():
    """ Should call Buffer for a given POST request. """

    mocked_session = MagicMock()
    mocked_session.post.return_value = MOCKED_RESPONSE

    with patch("buffpy.api.OAuth2Session", return_value=mocked_session):
        api = API(client_id="1", client_secret="2", access_token="access_token")
        api.post(url="hey", data="new=True")

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    mocked_session.post.assert_called_once_with(
        url="https://api.bufferapp.com/1/hey", headers=headers, data="new=True")


def test_api_post_request_no_access_token():
    """ Should raise ValueError if the API is called without an access_token. """

    with patch("buffpy.api.OAuth2Session", return_value=MagicMock(access_token=None)), \
            pytest.raises(ValueError):
        api = API(client_id="1", client_secret="2", access_token="access_token")
        api.post(url="hey", data="new=True")


def test_api_info():
    """ Should request Buffer's configuration. """

    mocked_session = MagicMock()
    mocked_session.get.return_value = MOCKED_RESPONSE

    with patch("buffpy.api.OAuth2Session", return_value=mocked_session):
        api = API(client_id="1", client_secret="2", access_token="access_token")
        info = api.info

        expected_url = "https://api.bufferapp.com/1/info/configuration.json"
        mocked_session.get.assert_called_once_with(url=expected_url)

        assert info.status == "ok"


@httpretty.activate
def test_api_post_parse_buffpy_error():
    """ Should raise a BuffpyRestException, if the API's response is >= 400. """

    httpretty.register_uri(httpretty.POST, "https://api.bufferapp.com/1/hey", status=400)

    with pytest.raises(BuffpyRestException):
        api = API(client_id="1", client_secret="2", access_token="access_token")
        api.post(url="hey", data="new=True")
