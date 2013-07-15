from buffpy.api import API

# check http://bufferapp.com/developers/apps to retrieve a token
# or generate one with the example
token = 'awesome_token'

# instantiate the api object
api = API(client_id='client_id',
          client_secret='client_secret',
          access_token=token)

# get api's info
print api.info
