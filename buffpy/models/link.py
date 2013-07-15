from buffpy.response import ResponseObject

PATHS = {
  'GET_SHARES': 'links/shares.json?url=%s'
}

class Link(ResponseObject):
  '''
    A link represents a unique URL that has been shared through Buffer
  '''

  def __init__(self, api, url):
    shares = api.get(url=PATHS['GET_SHARES'] % url)['shares']

    super(Link, self).__init__({'shares': shares, 'url': url})
    self.api = api

  def get_shares(self):
    '''
      Returns an object with a the numbers of shares a link has had using
      Buffer.

      www will be stripped, but other subdomains will not.
    '''

    self.shares = self.api.get(url=PATHS['GET_SHARES'] % self.url)['shares']

    return self.shares
