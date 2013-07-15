from pprint import pprint as pp

from colorama import Fore

from buffpy.models.update import Update
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

# retrieve a single update based on an id
update = Update(api=api, id='update_id')
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
