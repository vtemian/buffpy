from pprint import pprint as pp

from colorama import Fore

from buffpy.managers.profiles import Profiles
from buffpy.api import API

# check http://bufferapp.com/developers/apps to retrieve a token
# or generate one with the example
token = 'awesome_token'

# instantiate the api object
api = API(client_id='client_id',
          client_secret='client_secret',
          access_token=token)

# get all profiles
profiles = Profiles(api=api)
print profiles.all()

# filter profiles using some criteria
profile = Profiles(api=api).filter(service='twitter')[0]
print profile

# get schedules of my twitter profile
profile = Profiles(api=api).filter(service='twitter')[0]
print profile.schedules

# update schedules times for my twitter profile
profile = Profiles(api=api).filter(service='twitter')[0]

profile.schedules = {
  'days': ['tue', 'thu'],
  'times': ['13:45']
}
