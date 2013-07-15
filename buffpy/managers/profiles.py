from buffpy.models.profile import PATHS, Profile

class Profiles(list):
  '''
    Manage profiles
      + all     -> get all the profiles from buffer
      + filter  -> wrapper for list filtering
  '''

  def __init__(self, api, *args, **kwargs):
    super(Profiles, self).__init__(*args, **kwargs)

    self.api = api

  def all(self):
    '''
      Get all social newtworks profiles
    '''

    response = self.api.get(url=PATHS['GET_PROFILES'])

    for raw_profile in response:
      self.append(Profile(self.api, raw_profile))

    return self

  def filter(self, **kwargs):
    '''
      Based on some criteria, filter the profiles and return a new Profiles
      Manager containing only the chosen items

      If the manager doen't have any items, get all the profiles from Buffer
    '''

    if not len(self):
      self.all()

    new_list = filter(lambda item: [True for arg in kwargs if item[arg] == kwargs[arg]] != [], self)

    return Profiles(self.api, new_list)
