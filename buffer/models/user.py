from buffer.response import ResponseObject

class User(ResponseObject):
  REQUEST_URL = 'user.json'

  def __init__(self, api):
    response = api.get(url=self.REQUEST_URL)

    super(User, self).__init__(response)
