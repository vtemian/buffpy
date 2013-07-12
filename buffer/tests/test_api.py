import json

from nose.tools import eq_, raises
from mock import MagicMock, patch

from buffer.api import API

def test_api_info_request():
  '''
    Test simply api info request
  '''

  with patch('buffer.api.OAuth2Session') as mocked_session:

    mocked_response = MagicMock()
    mocked_response.content = json.dumps({'status': 'ok'})
    mocked_session.get.return_value = mocked_response

    mocked_session.access_token = 'access_token'

    api = API(client_id='1', client_secret='2', access_token='access_token')

    api.get(url="hey")
