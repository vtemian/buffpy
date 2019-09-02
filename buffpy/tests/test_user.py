from unittest.mock import MagicMock, patch

from buffpy.models.user import User


def test_simple_user_request():
    """
        Test to see if the api is called when a user request is made
    """

    mocked_response = {
        "key": "value"
    }
    mocked_api = MagicMock(get=MagicMock(return_value=mocked_response))

    with patch("buffpy.models.user.ResponseObject") as mocked_response:
        User(api=mocked_api)

        mocked_api.get.assert_called_once_with(url="user.json")
