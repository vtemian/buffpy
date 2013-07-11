from buffer.response import ResponseObject

PATHS = {
  'GET_UPDATE': 'updates/%s.json',
  'GET_INTERACTIONS': 'updates/%s/interactions.json',
  'EDIT': 'updates/%s/update.json',
  'PUBLISH': 'updates/%s/share.json',
  'DELETE': 'updates/%s/destroy.json',
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

  def edit(self, text, media=None, utc=None, now=None):
    '''
      Edit an existing, individual status update.
    '''

    url = PATHS['EDIT'] % self.id

    post_data = "text=%s&" % text

    if now:
      post_data += "now=%s&" % now

    if utc:
      post_data += "utc=%s&" % utc

    if media:
      media_format = "media[%s]=%s&"

      for media_type, media_item in media.iteritems():
        post_data += media_format % (media_type, media_item)

    return Update(api=self.api, raw_response=self.api.post(url=url,
      data=post_data)['update'])

  def publish(self):
    '''
      Immediately shares a single pending update and recalculates times for
      updates remaining in the queue.
    '''

    url = PATHS['PUBLISH'] % self.id
    return self.api.post(url=url)

  def delete(self):
    '''
      Permanently delete an existing status update.
    '''

    url = PATHS['DELETE'] % self.id
    return self.api.post(url=url)
