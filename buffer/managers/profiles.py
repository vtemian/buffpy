import json

from buffer.models.profile import PATHS, Profile

class Profiles(list):

  def __init__(self, api):
    self.api = api
  
  def all(self):
    response = self.api.get(url=PATHS['GET_PROFILES'], parser=json.loads)

    for raw_profile in response:
      self.append(Profile(self.api, raw_profile))

    return self
