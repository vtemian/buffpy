from buffer.api import API

from buffer.user import User

token = '1/714ebdb617705ef9491a81fb21c1da42'
api = API(client_id='51cc6dd5f882a8ba18000055', client_secret='83b019d154cae4d2c734d813b33e5e53', access_token=token)

user = User(api=api)
print user.id
