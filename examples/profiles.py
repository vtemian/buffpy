from pprint import pprint as pp

from colorama import Fore

from buffer.managers.profiles import Profiles
from buffer.api import API

# check http://bufferapp.com/developers/apps to retrieve a token
# or generate one with the example
token = '1/714ebdb617705ef9491a81fb21c1da42'

# instantiate the api object
api = API(client_id='51cc6dd5f882a8ba18000055', 
          client_secret='83b019d154cae4d2c734d813b33e5e53', 
          access_token=token)

# get all profiles 
#profiles = Profiles(api=api)
#print profiles.all()

# filter profiles using some criteria
#profile = Profiles(api=api).filter(service='twitter')[0]
#print profile

# get schedules of my twitter profile
profile = Profiles(api=api).filter(service='twitter')[0]
print profile.schedules

