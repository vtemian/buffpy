from pprint import pprint as pp

from colorama import Fore

from buffpy.managers.profiles import Profiles
from buffpy.managers.updates import Updates

from buffpy.api import API

# check http://bufferapp.com/developers/apps to retrieve a token
# or generate one with the example
token = 'awesome_token'

# instantiate the api object
api = API(client_id='client_id',
          client_secret='client_secret',
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
print profile.updates.reorder(['update_id'])

# create an update
print profile.updates.new("Hello there", now=True)
