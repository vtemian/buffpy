from rauth import OAuth2Session

BASE_URL = 'https://api.bufferapp.com/'

class API(object):
  '''
    Small and clean class that embrace all basic 
    operations with the buffer app
  '''

  def __init__(self, client_id, client_secret, access_token=None):
    self.session = OAuth2Session(client_id, client_secret, access_token)

    self.call_url = None
    if access_token:
      self.set_access_token(access_token)

  def set_access_token(self, access_token=None):
    if not access_token or not isinstance(access_token, str):
      raise ValueError('The access token is missing or is invalid')

    self.call_url = BASE_URL + "%saccess_token=" + access_token
