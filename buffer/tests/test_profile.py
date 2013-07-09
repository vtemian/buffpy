import json

from nose.tools import eq_, raises
from mock import MagicMock, patch

from buffer.models.profile import Profile, PATHS

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
  mocked_api.get.assert_called_once_with(url = PATHS['GET_SCHEDULES'] % 1, parser=json.loads)
