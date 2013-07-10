import json

from rauth import OAuth2Session

BASE_URL = 'https://api.bufferapp.com/1/%s'

class API(OAuth2Session):
  '''
    Small and clean class that embrace all basic
    operations with the buffer app
  '''

  def get(self, url, parser=None):
    if parser == None:
      parser = json.loads

    if not self.access_token:
      raise ValueError('Please set an access token first!')

    response = super(OAuth2Session, self).get(url=BASE_URL % url)

    return parser(response.content)

  def post(self, url, parser=None, **params):
    if parser == None:
      parser = json.loads

    if not self.access_token:
      raise ValueError('Please set an access token first!')

    headers = {'Content-Type':'application/x-www-form-urlencoded'}

    response = super(OAuth2Session, self).post(url=BASE_URL % url, headers=headers, **params)

    return parser(response.content)

  def put(self, url, params, parser=None):
    if parser == None:
      parser = json.loads

    pass

  def delete(self, url, params):
    pass
