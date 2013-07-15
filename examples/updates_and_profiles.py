from pprint import pprint as pp

from colorama import Fore

from buffer.managers.profiles import Profiles
from buffer.managers.updates import Updates

from buffer.api import API

# check http://bufferapp.com/developers/apps to retrieve a token
# or generate one with the example
token = '1/714ebdb617705ef9491a81fb21c1da42'

# instantiate the api object
api = API(client_id='51cc6dd5f882a8ba18000055',
          client_secret='83b019d154cae4d2c734d813b33e5e53',
          access_token=token)

# get all pending updates of a social network profile
profile = Profiles(api=api).filter(service='twitter')[0]
print profile.updates.pending

# get all sent updates of a social network profile
print profile.updates.sent

# retrieve all update's interactions
print profile.updates.sent[0].interactions

# shuffle updates
print profile.updates.shuffle(count=10)

# reorder updates
print profile.updates.reorder(['51dd27629f7fdf520d00009a'])

# create an update
print profile.updates.new("Hello there", now=True)
