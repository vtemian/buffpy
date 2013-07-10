from buffer.models.update import Update

PATHS = {
  'GET_PENDING': 'profiles/%s/updates/pending.json',
  'GET_SENT': 'profiles/%s/updates/sent.json',
  'SHUFFLE': 'profiles/%s/updates/shuffle.json',
}

class Updates(list):

  def __init__(self, api, profile_id):
    self.api = api
    self.profile_id = profile_id

    self.__pending = []
    self.__sent = []

  @property
  def pending(self):
    '''
      Returns an array of updates that are currently in the buffer for an
      individual social media profile.
    '''

    pending_updates = []
    url = PATHS['GET_PENDING'] % self.profile_id

    response = self.api.get(url=url)
    for update in response['updates']:
      pending_updates.append(update(api=self.api, raw_response=update))

    self.__pending = pending_updates

    return self.__pending

  @property
  def sent(self):
    '''
      Returns an array of updates that have been sent from the buffer for an
      individual social media profile.
    '''

    sent_updates = []
    url = PATHS['GET_SENT'] % self.profile_id

    response = self.api.get(url=url)
    for update in response['updates']:
      sent_updates.append(Update(api=self.api, raw_response=update))

    self.__sent = sent_updates

    return self.__sent

  def shuffle(self, count=None, utc=None):
    '''
      Randomize the order at which statuses for the specified social media
      profile will be sent out of the buffer.
    '''

    url = PATHS['SHUFFLE'] % self.profile_id

    post_data = ''
    if count:
      post_data += 'count=%s&' % count
    if utc:
      post_data += 'utc=%s' % utc

    return self.api.post(url=url, data=post_data)
