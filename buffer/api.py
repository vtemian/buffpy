import json

from rauth import OAuth2Session

from buffer.response import ResponseObject

BASE_URL = 'https://api.bufferapp.com/1/%s'
PATHS = {
  'INFO': 'info/configuration.json'
}

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

  @property
  def info(self):
    '''
      Returns an object with the current configuration that Buffer is using,
      including supported services, their icons and the varying limits of
      character and schedules.

      The services keys map directly to those on profiles and updates so that
      you can easily show the correct icon or calculate the correct character
      length for an update.
    '''

    response = self.get(url=PATHS['INFO'])
    return ResponseObject(response)
