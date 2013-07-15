from buffpy.response import ResponseObject

class User(ResponseObject):
  '''
    A user represents a single Buffer user account.
  '''

  REQUEST_URL = 'user.json'

  def __init__(self, api):
    response = api.get(url=self.REQUEST_URL)

    super(User, self).__init__(response)
