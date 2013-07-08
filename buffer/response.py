class ResponseObject(dict):

  def __init__(self, *args, **kwargs):
    super(ResponseObject, self).__init__(*args, **kwargs)

    self.__dict__ = self._check_for_inception(self)

  def _check_for_inception(self, root_dict):

    for key in root_dict:
      if type(root_dict[key]) == dict:
          root_dict[key] = ResponseObject(root_dict[key])

    return root_dict

  def set_for(self, cls):
    cls.__dict__ = self.__dict__
