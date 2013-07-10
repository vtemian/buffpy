from buffer.response import ResponseObject

PATHS = {
  'GET_UPDATE': 'updates/%s.json',
  'GET_INTERACTIONS': 'updates/%s/interactions.json',
}

class Update(ResponseObject):

  def __init__(self, api, id=None, raw_response=None):

    if id and not raw_response:
      raw_response = api.get(url=PATHS['GET_UPDATE'] % id)

    super(Update, self).__init__(raw_response)

    self.api = api
    self.__interactions = []

  @property
  def interactions(self):
    '''
      Returns the detailed information on individual interactions with the social
      media update such as favorites, retweets and likes.
    '''

    interactions = []
    url = PATHS['GET_INTERACTIONS'] % self.id

    response = self.api.get(url=url)
    for interaction in response['interactions']:
      interactions.append(ResponseObject(interaction))

    self.__interactions = interactions

    return self.__interactions
