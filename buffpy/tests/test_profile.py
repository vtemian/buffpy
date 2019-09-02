from unittest.mock import MagicMock, patch

from buffpy.models.profile import Profile, PATHS


MOCKED_RESPONSE = {
    "name": "me",
    "service": "twiter",
    "id": 1
}


def test_profile_schedules_getter():
    """ Should retrieve profiles from buffer's API. """

    mocked_api = MagicMock()
    mocked_api.get.return_value = "123🏳️‍🌈"

    profile = Profile(mocked_api, MOCKED_RESPONSE)

    assert profile.schedules == "123🏳️‍🌈"
    mocked_api.get.assert_called_once_with(url=PATHS["GET_SCHEDULES"].format("1"))


def test_profile_schedules_setter():
    """ Should update profile's schedules. """

    mocked_api = MagicMock()
    mocked_api.get.return_value = "123"

    profile = Profile(mocked_api, MOCKED_RESPONSE)

    profile.schedules = {
        "times": ["mo"]
    }

    mocked_api.post.assert_called_once_with(
        url=PATHS["UPDATE_SCHEDULES"].format("1"),
        data="schedules[0][times][]=mo&")


def test_profile_updates():
    """ Should properly call buffer's updates. """

    mocked_api = MagicMock()

    with patch("buffpy.managers.updates.Updates") as mocked_updates:
        profile = Profile(api=mocked_api, raw_response={"id": 1})

        assert profile.updates
        mocked_updates.assert_called_once_with(api=mocked_api, profile_id=1)
