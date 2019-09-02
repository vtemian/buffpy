import json
from collections import OrderedDict
from unittest.mock import MagicMock, patch

from buffpy.managers.updates import Updates
from buffpy.models.update import Update


def test_updates_manager_pending():
    """
        Test basic pending updates retrieving
    """

    mocked_api = MagicMock()
    mocked_api.get.return_value = {
        "updates": [{
            "text": "hey"
        }]
    }

    pendings = Updates(api=mocked_api, profile_id=1).pending

    mocked_api.get.assert_called_once_with(url="profiles/1/updates/pending.json")
    assert pendings == [Update(api=mocked_api, raw_response={"text": "hey"})]


def test_udpates_manager_sent():
    """
        Test basic sent updates retrieving
    """

    mocked_api = MagicMock()
    mocked_api.get.return_value = {
        "updates": [{
            "text": "sent"
        }]
    }

    sent = Updates(api=mocked_api, profile_id=1).sent
    assert_update = Update(api=mocked_api, raw_response={"text": "sent"})

    mocked_api.get.assert_called_once_with(url="profiles/1/updates/sent.json")
    assert sent == [assert_update]


def test_udpates_manager_suffle():
    """
        Test basic updates shuffle
    """

    mocked_api = MagicMock()
    mocked_api.post.return_value = True

    assert Updates(api=mocked_api, profile_id=1).shuffle()
    mocked_api.post.assert_called_once_with(url="profiles/1/updates/shuffle.json", data="")


def test_udpates_manager_suffle_with_params():
    """
        Test updates shuffling with count and utc params
    """

    mocked_api = MagicMock()
    mocked_api.post.return_value = True

    assert Updates(api=mocked_api, profile_id=1).shuffle(count=10, utc="hey")
    mocked_api.post.assert_called_once_with(url="profiles/1/updates/shuffle.json",
                                            data="count=10&utc=hey")


def test_updates_manager_reorder():
    """
        Test basic updates reorder
    """

    mocked_api = MagicMock()
    mocked_api.post.return_value = True

    assert Updates(api=mocked_api, profile_id=1).reorder([1, 2])
    mocked_api.post.assert_called_once_with(url="profiles/1/updates/reorder.json",
                                            data="order[]=1&order[]=2&")


def test_updates_manager_reorder_with_params():
    """
        Test basic updates reorder with params
    """

    mocked_api = MagicMock()
    mocked_api.post.return_value = True

    assert Updates(api=mocked_api, profile_id=1).reorder([1, 2], 10, "hey")
    mocked_api.post.assert_called_once_with(url="profiles/1/updates/reorder.json",
                                            data="offset=10&utc=hey&order[]=1&order[]=2&")


def test_updates_manager_new_update():
    """
        Test update creation
    """

    mocked_api = MagicMock()
    mocked_api.post.return_value = {"updates": [{"text": "hey"}]}

    updates = Updates(api=mocked_api, profile_id=1)
    update = updates.new("hey")

    data = "text=hey&profile_ids[]=1&"
    mocked_api.post.assert_called_once_with(url="updates/create.json", data=data)

    assert_update = Update(api=mocked_api, raw_response={"text": "hey"})
    assert update == assert_update
    assert assert_update in updates


def test_updates_manager_new_update_all_params():
    """
        Test update creation with all params
    """

    mocked_api = MagicMock()
    raw_update = OrderedDict({
        "text": "hey",
        "shorten": True,
        "now": True,
        "top": True,
        "media": OrderedDict({
            "link": "www.google.com",
            "photo": "www.google.ro"
        })
    })

    assert Updates(api=mocked_api, profile_id=1).new(**raw_update)

    data = "text=hey&profile_ids[]=1&shorten=True&now=True&top=True&" + \
           "media[link]=www.google.com&media[photo]=www.google.ro&"
    mocked_api.post.assert_called_once_with(url="updates/create.json", data=data)
