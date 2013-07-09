import json

from rauth import OAuth2Session

BASE_URL = 'https://api.bufferapp.com/1/%s'

class API(OAuth2Session):
  '''
    Small and clean class that embrace all basic 
    operations with the buffer app
  '''

  def get(self, url, parser):
    if not self.access_token:
      raise ValueError('Please set an access token first!')

    response = super(OAuth2Session, self).get(url=BASE_URL % url)

    return parser(response.content)

  def post(self, url, params, parser):
    pass

  def put(self, url, params, parser):
    pass

  def delete(self, url, params):
    pass
