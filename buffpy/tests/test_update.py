from nose.tools import eq_
from mock import MagicMock

from buffpy.models.update import Update, PATHS

def test_update_retrieving():
  '''
    Test basic update retrieving based on update's id
  '''

  mocked_api = MagicMock()
  mocked_api.get.return_value = {
    'text': 'me',
    'id': 1
  }

  update = Update(api=mocked_api, id=1)

  mocked_api.get.assert_called_once_with(url='updates/1.json')
  eq_(update.api, mocked_api)
  eq_(update.text, 'me')

def test_update_interactions():
  '''
    Test basic analytics retrieving
  '''

  mocked_api = MagicMock()
  mocked_api.get.return_value = {'interactions': [{'replies': 3}]}

  update = Update(mocked_api, raw_response={'id': 1, 'text': 'hey'})

  eq_(update.interactions, [{'replies': 3}])
  mocked_api.get.assert_called_once_with(url='updates/1/interactions.json')

def test_update_edit():
  '''
    Test basic update editing
  '''

  mocked_api = MagicMock()
  mocked_api.post.return_value = {
      'update': {'id': 1, 'text': 'hey!'}
  }

  update = Update(mocked_api, raw_response={'id':1, 'text': 'ola!'})
  new_update = update.edit(text='hey!')

  assert_update = Update(mocked_api, raw_response={'id':1, 'text': 'hey!'})

  post_data = 'text=hey!&'
  mocked_api.post.assert_called_once_with(url='updates/1/update.json',
      data=post_data)
  eq_(new_update, assert_update)

def test_update_edit_params():
  '''
    Test basic update editing with all the params
  '''

  mocked_api = MagicMock()
  mocked_api.post.return_value = {
      'update': {'id': 1, 'text': 'hey!'}
  }

  update = Update(mocked_api, raw_response={'id':1, 'text': 'ola!'})
  new_update = update.edit(text='hey!', media={'link':'w'}, utc="a", now=True)

  assert_update = Update(mocked_api, raw_response={'id':1, 'text': 'hey!'})

  post_data = 'text=hey!&now=True&utc=a&media[link]=w&'
  mocked_api.post.assert_called_once_with(url='updates/1/update.json',
      data=post_data)
  eq_(new_update, assert_update)

def test_udpate_publishing():
  '''
    Test basic update publishing
  '''

  mocked_api = MagicMock()
  mocked_api.post.return_value = True

  response = Update(api=mocked_api, raw_response={'id': 1}).publish()

  mocked_api.post.assert_called_once_with(url="updates/1/share.json")
  eq_(response, True)

def test_update_deleting():
  '''
    Test update's deleting
  '''

  mocked_api = MagicMock()
  mocked_api.post.return_value = True

  response = Update(api=mocked_api, raw_response={'id': 1}).delete()

  mocked_api.post.assert_called_once_with(url='updates/1/destroy.json')
  eq_(response, True)

def test_update_move_to_top():
  '''
    Test move_to_top implementation
  '''

  mocked_api = MagicMock()
  mocked_api.post.return_value = {'id': 1, 'text': 'hey'}

  response = Update(api=mocked_api, raw_response={'id': 1}).move_to_top()

  mocked_api.post.assert_called_once_with(url='updates/1/move_to_top.json')
  eq_(response.text, 'hey')
