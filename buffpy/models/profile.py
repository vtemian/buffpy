from buffpy.response import ResponseObject
from buffpy.managers.updates import Updates

PATHS = {
  'GET_PROFILES': 'profiles.json',
  'GET_PROFILE': 'profiles/%s.json',
  'GET_SCHEDULES': 'profiles/%s/schedules.json',
  'UPDATE_SCHEDULES': 'profiles/%s/schedules/update.json'
}

class Profile(ResponseObject):
  '''
    A Buffer profile represents a connection to a single social media account.
  '''

  def __init__(self, api, raw_response):
    super(Profile, self).__init__(raw_response)

    self.api = api
    self.__schedules = None

  @property
  def schedules(self):
    '''
      Returns details of the posting schedules associated with a social media
      profile.
    '''

    url = PATHS['GET_SCHEDULES'] % self.id

    self.__schedules = self.api.get(url=url)

    return self.__schedules

  @schedules.setter
  def schedules(self, schedules):
    '''
      Set the posting schedules for the specified social media profile.
    '''

    url = PATHS['UPDATE_SCHEDULES'] % self.id

    data_format = "schedules[0][%s][]=%s&"
    post_data = ""

    for format_type, values in schedules.iteritems():
      for value in values:
        post_data += data_format % (format_type, value)

    self.api.post(url=url, data=post_data)

  @property
  def updates(self):
    return Updates(api=self.api, profile_id=self.id)
