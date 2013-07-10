from buffer.response import ResponseObject

PATHS = {
  'GET_UPDATE': 'updates/%s.json',
}

class Update(ResponseObject):

  def __init__(self, api, id=None, raw_response=None):
    self.api = api

    if id and not raw_response:
      raw_response = self.api.get(url=PATHS['GET_UPDATE'] % id)

    super(Update, self).__init__(raw_response)
