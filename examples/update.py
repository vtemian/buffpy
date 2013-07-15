from pprint import pprint as pp

from colorama import Fore

from buffpy.models.update import Update
from buffpy.managers.profiles import Profiles
from buffpy.managers.updates import Updates
from buffpy.api import API

# check http://bufferapp.com/developers/apps to retrieve a token
# or generate one with the example
token = '1/714ebdb617705ef9491a81fb21c1da42'

# instantiate the api object
api = API(client_id='51cc6dd5f882a8ba18000055',
          client_secret='83b019d154cae4d2c734d813b33e5e53',
          access_token=token)

# retrieve a single update based on an id
update = Update(api=api, id='51de8d33e48c051712000019')
print update

# get update's interactions
print update.interactions

# edit
update = update.edit(text="Hey!")

# publish now
update.publish()

# move to top
update.move_to_top()

# delete
update.delete()
