from rauth import OAuth2Session

BASE_URL = 'https://api.bufferapp.com/1/%s'

class API(OAuth2Session):
  '''
    Small and clean class that embrace all basic 
    operations with the buffer app
  '''

  def get(self, url):
    if not self.access_token:
      raise ValueError('Please set an access token first!')

    return super(OAuth2Session, self).get(url=BASE_URL % url)
