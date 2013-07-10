from buffer.models.update import Update

PATHS = {
  'GET_PENDING': 'profiles/%s/updates/pending.json',
}

class Updates(list):

  def __init__(self, api, profile_id):
    self.api = api
    self.profile_id = profile_id

  @property
  def pending(self):
    url = PATHS['GET_PENDING'] % self.profile_id

    response = self.api.get(url=url)
    for update in response['updates']:
      self.append(Update(api=self.api, raw_response=update))

    return self
