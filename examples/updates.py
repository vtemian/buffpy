from pprint import pprint as pp

from colorama import Fore

from buffer.models.update import Update
from buffer.api import API

# check http://bufferapp.com/developers/apps to retrieve a token
# or generate one with the example
token = '1/714ebdb617705ef9491a81fb21c1da42'

# instantiate the api object
api = API(client_id='51cc6dd5f882a8ba18000055', 
          client_secret='83b019d154cae4d2c734d813b33e5e53', 
          access_token=token)

update = Update(api=api, id='51dd27629f7fdf520d00009a')
print update
