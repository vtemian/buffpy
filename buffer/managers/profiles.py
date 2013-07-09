import json

from buffer.models.profile import PATHS, Profile

class Profiles(list):

  def __init__(self, api, *args, **kwargs):
    super(Profiles, self).__init__(*args, **kwargs)

    self.api = api

  def all(self):
    response = self.api.get(url=PATHS['GET_PROFILES'], parser=json.loads)

    for raw_profile in response:
      self.append(Profile(self.api, raw_profile))

    return self

  def filter(self, **kwargs):

    if not len(self):
      self.all()

    new_list = filter(lambda item: [True for arg in kwargs if item[arg] == kwargs[arg]] != [], self)

    return Profiles(self.api, new_list)
