from buffpy.models.link import Link
from buffpy.api import API

# check http://bufferapp.com/developers/apps to retrieve a token
# or generate one with the example
token = 'awesome_tokne'

# instantiate the api object
api = API(client_id='client_id',
          client_secret='client_secret',
          access_token=token)

# get a link's shares
print Link(api=api, url='http%3A%2F%2Fbufferapp.com').shares
