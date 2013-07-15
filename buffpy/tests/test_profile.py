from nose.tools import eq_
from mock import MagicMock, patch

from buffpy.models.profile import Profile, PATHS

mocked_response = {
  'name': 'me',
  'service': 'twiter',
  'id': 1
}

def test_profile_schedules_getter():
  '''
    Test schedules gettering from buffer api
  '''

  mocked_api = MagicMock()
  mocked_api.get.return_value = '123'

  profile = Profile(mocked_api, mocked_response)

  eq_(profile.schedules, '123')
  mocked_api.get.assert_called_once_with(url = PATHS['GET_SCHEDULES'] % 1)

def test_profile_schedules_setter():
  '''
    Test schedules setter from buffer api
  '''

  mocked_api = MagicMock()
  mocked_api.get.return_value = '123'

  profile = Profile(mocked_api, mocked_response)

  profile.schedules = {
      'times': ['mo']
  }

  mocked_api.post.assert_called_once_with(url=PATHS['UPDATE_SCHEDULES'] % 1,
      data='schedules[0][times][]=mo&')

def test_profile_updates():
  '''
    Test updates relationship with a profile
  '''

  mocked_api = MagicMock()

  with patch('buffpy.models.profile.Updates') as mocked_updates:
    profile = Profile(api=mocked_api, raw_response={'id': 1})
    updates = profile.updates

    mocked_updates.assert_called_once_with(api=mocked_api, profile_id=1)
