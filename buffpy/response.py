class ResponseObject(dict):
  '''
    Simple data structure that convert any dict to an empty object
    where all the atributes are the keys of the dict, but also preserve a dict
    behavior
    e.g:

      obj = ResponseObject({'a':'b'})
      obj.key = 'value'

      obj.a   => 'b'
      obj     => {'a': 'b', 'key': 'value'}
  '''

  def __init__(self, *args, **kwargs):
    super(ResponseObject, self).__init__(*args, **kwargs)

    self.__dict__ = self._check_for_inception(self)

  def _check_for_inception(self, root_dict):
    '''
      Used to check if there is a dict in a dict
    '''

    for key in root_dict:
      if isinstance(root_dict[key], dict):
          root_dict[key] = ResponseObject(root_dict[key])

    return root_dict
