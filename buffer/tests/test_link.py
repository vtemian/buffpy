from nose.tools import eq_, raises
from mock import MagicMock, patch

from buffer.models.link import Link

def test_links_shares():
  '''
    Test link's shares retrieving from constructor
  '''

  mocked_api = MagicMock()
  mocked_api.get.return_value = {'shares': 123}

  link = Link(api=mocked_api, url='www.google.com')

  eq_(link, {'shares': 123, 'url': 'www.google.com', 'api': mocked_api})
