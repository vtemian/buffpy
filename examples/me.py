from pprint import pprint as pp

from colorama import Fore

from buffer.api import API
from buffer.user import User

# check http://bufferapp.com/developers/apps to retrieve a token
# or generate one with the example
token = '1/714ebdb617705ef9491a81fb21c1da42'

# instantiate the api object
api = API(client_id='51cc6dd5f882a8ba18000055', 
          client_secret='83b019d154cae4d2c734d813b33e5e53', 
          access_token=token)

# instantiate an user object
user = User(api=api)

# now play!
print Fore.YELLOW + '<< Just the basic user obj as dict >>\n' + Fore.RESET, user
print Fore.YELLOW + '<< User\'s ID >>\n' + Fore.RESET, user.id
print Fore.YELLOW + '<< User\'s timezone >>\n' + Fore.RESET, user.timezone
