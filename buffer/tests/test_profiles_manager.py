import json

from nose.tools import eq_, raises
from mock import MagicMock, patch

from buffer.managers.profiles import Profiles
from buffer.models.profile import PATHS

mocked_response = {
  'name': 'me',
  'service': 'twiter',
  'id': 1
}

def test_profiles_manager_all_method():
  '''
    Test basic profiles retrieving
  '''

  mocked_api = MagicMock()
  mocked_api.get.return_value = [{'a':'b'}]

  with patch('buffer.managers.profiles.Profile') as mocked_profile:
    mocked_profile.return_value = 1

    profiles = Profiles(api=mocked_api).all()

    eq_(profiles, [1])
    mocked_api.get.assert_called_once_with(url=PATHS['GET_PROFILES'],
        parser=json.loads)
    mocked_profile.assert_called_once_with(mocked_api, {'a': 'b'})
