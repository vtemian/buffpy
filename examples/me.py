from pprint import pprint as pp

from colorama import Fore

from buffpy.api import API
from buffpy.models.user import User

# check http://bufferapp.com/developers/apps to retrieve a token
# or generate one with the example
token = 'awesome_token'

# instantiate the api object
api = API(client_id='client_id', 
          client_secret='client_secret', 
          access_token=token)

# instantiate an user object
user = User(api=api)

# now play!
print Fore.YELLOW + '<< Just the basic user obj as dict >>\n' + Fore.RESET, user
print Fore.YELLOW + '<< User\'s ID >>\n' + Fore.RESET, user.id
print Fore.YELLOW + '<< User\'s timezone >>\n' + Fore.RESET, user.timezone
