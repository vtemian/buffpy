from nose.tools import eq_
from mock import MagicMock, patch

from buffpy.managers.profiles import Profiles
from buffpy.models.profile import Profile, PATHS

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

  with patch('buffpy.managers.profiles.Profile') as mocked_profile:
    mocked_profile.return_value = 1

    profiles = Profiles(api=mocked_api).all()

    eq_(profiles, [1])
    mocked_api.get.assert_called_once_with(url=PATHS['GET_PROFILES'])
    mocked_profile.assert_called_once_with(mocked_api, {'a': 'b'})

def test_profiles_manager_filter_method():
  '''
    Test basic profiles filtering based on some minimal criteria
  '''

  mocked_api = MagicMock()

  profiles = Profiles(mocked_api, [{'a':'b'}, {'a': 'c'}])

  eq_(profiles.filter(a='b'), [{'a': 'b'}])

def test_profiles_manager_filter_method_empty():
  '''
    Test basic profiles filtering when the manager is empty
  '''

  mocked_api = MagicMock()
  mocked_api.get.return_value = [{'a':'b'}, {'a': 'c'}]


  profiles = Profiles(api=mocked_api)

  eq_(profiles.filter(a='b'), [Profile(mocked_api, {'a': 'b'})])
