from unittest.mock import MagicMock

from buffpy.models.link import Link


def test_links_shares():
    """ Test link"s shares retrieving from constructor. """

    mocked_api = MagicMock()
    mocked_api.get.return_value = {"shares": 123}

    link = Link(api=mocked_api, url="www.google.com")

    assert link["shares"] == 123
    assert link["url"] == "www.google.com"
    mocked_api.get.assert_called_once_with(url="links/shares.json?url=www.google.com")


def test_links_get_shares():
    """ Test link"s shares retrieving method. """

    mocked_api = MagicMock()
    mocked_api.get.return_value = {"shares": 123}

    link = Link(api=mocked_api, url="www.google.com")

    assert link["shares"] == 123
    assert link["url"] == "www.google.com"
    assert link.get_shares() == 123

    mocked_api.get.assert_any_call(url="links/shares.json?url=www.google.com")
    assert mocked_api.get.call_count == 2
