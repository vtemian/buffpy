import json

from nose.tools import eq_, raises
from mock import MagicMock, patch

from buffer.api import API

def test_api_get_request():
  '''
    Test simply api get request
  '''

  with patch('buffer.api.OAuth2Session') as mocked_oauth2:
    mocked_session = MagicMock()

    mocked_response = MagicMock()
    mocked_response.content = json.dumps({'status': 'ok'})
    mocked_session.get.return_value = mocked_response

    mocked_oauth2.return_value = mocked_session

    api = API(client_id='1', client_secret='2', access_token='access_token')

    api.get(url="hey")
