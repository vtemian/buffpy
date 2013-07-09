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

  def _post_schedules(self, schedules):
    url = PATHS['UPDATE_SCHEDULES'] % self.id

    data_format = "schedules[0][%s][]=%s&"
    post_data = ""

    for format_type, values in schedules.iteritems():
      for value in values:
        post_data += data_format % (format_type, value)

    self.api.post(url=url, parser=json.loads, data=post_data)

  def _get_schedules(self):
    url = PATHS['GET_SCHEDULES'] % self.id

    self.schedules = self.api.get(url=url, parser=json.loads)

    return self.schedules
