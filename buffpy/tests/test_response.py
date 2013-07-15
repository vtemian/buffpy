from nose.tools import eq_

from buffpy.response import ResponseObject

def test_reponse_check_for_inception():
  '''
    Given a dict with a dict, it should convert all the dicts to ResponseObject
  '''

  awesome_dict = {
    'key': 'value',
    'second_dict': {
      'key2': 'value2'
    }
  }

  response = ResponseObject(awesome_dict)
  response.key3 = 'value3'

  eq_(response.key, 'value')
  eq_(response.key3, 'value3')
  eq_(response.second_dict, {'key2': 'value2'})
  eq_(response.second_dict.key2, 'value2')
