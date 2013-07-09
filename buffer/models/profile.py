import json

from buffer.response import ResponseObject

PATHS = {
  'GET_PROFILES': 'profiles.json',
  'GET_PROFILE': 'profiles/%s.json',
  'GET_SCHEDULES': 'profiles/%s/schedules.json',
  'UPDATE_SCHEDULES': 'profiles/%s/schedules/update.json'
}

class Profile(ResponseObject):

  def __init__(self, api, raw_response):
    super(Profile, self).__init__(raw_response)

    self.api = api

  def __getattr__(self, name):
    if callable(name):
      name()

    if hasattr(self, name):
      return getattr(self, name)

    if hasattr(self, "_get_%s" % name):
      return getattr(self, "_get_%s" % name)()

  def _get_schedules(self):
    url = PATHS['GET_SCHEDULES'] % self.id

    self.schedules = self.api.get(url=url, parser=json.loads)

    return self.schedules
