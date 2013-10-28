from buffpy.models.update import Update

PATHS = {
  'GET_PENDING': 'profiles/%s/updates/pending.json',
  'GET_SENT': 'profiles/%s/updates/sent.json',
  'SHUFFLE': 'profiles/%s/updates/shuffle.json',
  'REORDER': 'profiles/%s/updates/reorder.json',
  'CREATE': 'updates/create.json',
}

class Updates(list):
  '''
    Implenents all the profiles+updates logic.

    + retrieve updates related to a profile
    + create a new update
    + reorder and shuffle updates
  '''

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
      pending_updates.append(Update(api=self.api, raw_response=update))

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

  def reorder(self, updates_ids, offset=None, utc=None):
    '''
      Edit the order at which statuses for the specified social media profile will
      be sent out of the buffer.
    '''

    url = PATHS['REORDER'] % self.profile_id

    order_format = "order[]=%s&"
    post_data = ''

    if offset:
      post_data += 'offset=%s&' % offset

    if utc:
      post_data += 'utc=%s&' % utc

    for update in updates_ids:
      post_data += order_format % update

    return self.api.post(url=url, data=post_data)

  #TODO: Multiple profile posting
  def new(self, text, shorten=None, now=None, top=None, media=None, when=None):
    '''
      Create one or more new status updates.
    '''

    url = PATHS['CREATE']

    post_data = "text=%s&" % text
    post_data += "profile_ids[]=%s&" % self.profile_id

    if shorten:
      post_data += "shorten=%s&" % shorten

    if now:
      post_data += "now=%s&" % now

    if top:
      post_data += "top=%s&" % top

    if when:
      post_data += "scheduled_at=%s&" % str(when)

    if media:
      media_format = "media[%s]=%s&"

      for media_type, media_item in media.iteritems():
        post_data += media_format % (media_type, media_item)

    response = self.api.post(url=url, data=post_data)
    new_update = Update(api=self.api, raw_response=response['updates'][0])

    self.append(new_update)

    return new_update
