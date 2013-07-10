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

def test_udpate_interactions():
  '''
    Test basic analytics retrieving
  '''

  mocked_api = MagicMock()
  mocked_api.get.return_value = {'interactions': [{'replies': 3}]}

  update = Update(mocked_api, raw_response={'id': 1, 'text': 'hey'})

  eq_(update.interactions, [{'replies': 3}])
  mocked_api.get.assert_called_once_with(url='updates/1/interactions.json')
