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
    self.api = api

    super(Profile, self).__init__(raw_response)
