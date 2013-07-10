import json

from nose.tools import eq_, raises
from mock import MagicMock, patch

from buffer.models.update import Update, PATHS

def test_update_retrieving():
  '''
    Test basic update retrieving based on update's id
  '''

  mocked_api = MagicMock()
  mocked_api.get.return_value = {
    'text': 'me',
    'id': 1
  }

  update = Update(api=mocked_api, id=1)

  mocked_api.get.assert_called_once_with(url='updates/1.json')
  eq_(update.api, mocked_api)
  eq_(update.text, 'me')
