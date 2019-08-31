from unittest.mock import MagicMock, patch

from buffpy.managers.profiles import Profiles
from buffpy.models.profile import Profile, PATHS


MOCKED_RESPONSE = {
    "name": "me",
    "service": "twiter",
    "id": 1
}


def test_profiles_manager_all_method():
    """ Should retrieve profile info. """

    mocked_api = MagicMock()
    mocked_api.get.return_value = [{"a": "b"}]

    with patch("buffpy.managers.profiles.Profile", return_value=1) as mocked_profile:
        profiles = Profiles(api=mocked_api).all()

        assert profiles == [1]
        mocked_api.get.assert_called_once_with(url=PATHS["GET_PROFILES"])
        mocked_profile.assert_called_once_with(mocked_api, {"a": "b"})


def test_profiles_manager_filter_method():
    """ Should filter based on criteria. """

    mocked_api = MagicMock()
    profiles = Profiles(mocked_api, [{"a": "b"}, {"a": "c"}])
    assert profiles.filter(a="b") == [{"a": "b"}]


def test_profiles_manager_filter_method_empty():
    """ Should filter if profile manager is None. """

    mocked_api = MagicMock()
    mocked_api.get.return_value = [{"a": "b"}, {"a": "c"}]

    profiles = Profiles(api=mocked_api)

    assert profiles.filter(a="b") == [Profile(mocked_api, {"a": "b"})]
