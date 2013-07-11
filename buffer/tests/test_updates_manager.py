import json

from nose.tools import eq_, raises
from mock import MagicMock, patch

from buffer.managers.updates import Updates
from buffer.models.update import Update

def test_updates_manager_pending():
  '''
    Test basic pending updates retrieving
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

def test_udpates_manager_sent():
  '''
    Test basic sent updates retrieving
  '''

  mocked_api = MagicMock()
  mocked_api.get.return_value = {
    'updates': [{
      'text': 'sent'
    }]
  }

  sent = Updates(api=mocked_api, profile_id=1).sent
  assert_update = Update(api=mocked_api, raw_response={'text': 'sent'})

  mocked_api.get.assert_called_once_with(url='profiles/1/updates/sent.json')
  eq_(sent, [assert_update])
