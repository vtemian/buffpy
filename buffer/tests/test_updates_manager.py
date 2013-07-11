import json

from nose.tools import eq_, raises
from mock import MagicMock, patch

from buffer.managers.updates import Updates
from buffer.models.update import Update

def test_updates_manager_pending():
  '''
    Test basic pending updates retreiving
  '''

  mocked_api = MagicMock()
  mocked_api.get.return_value = {
      'updates': [{
        'text': 'hey'
      }]
  }

  pendings = Updates(api=mocked_api, profile_id=1).pending

  mocked_api.get.assert_called_once_with(url='profiles/1/updates/pending.json')
  eq_(pendings, [Update(api=mocked_api, raw_response={'text': 'hey'})])
