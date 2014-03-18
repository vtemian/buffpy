buffer-app-python (buffpy)
==========================
Simple to use python library for Buffer App

[![Build Status](https://travis-ci.org/vtemian/buffpy.png?branch=master)](https://travis-ci.org/vtemian/buffpy) [![Coverage Status](https://coveralls.io/repos/vtemian/buffpy/badge.png?branch=master)](https://coveralls.io/r/vtemian/buffpy?branch=master)
[![Downloads](https://pypip.in/d/buffpy/badge.png)](https://crate.io/packages/buffpy/)
[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/vtemian/buffpy/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

### ORM`ish
------------
Bufferapp.com details some useful entities:
  * user
  * profile
  * update
  * link
  * info

Every entity can be seen as an object that has attributes and methods. Those
methdos and attributes are linked to certain endpoints.

All objects are special dicts. For example, you can do something like:
```python
user.id     => '12455678976asd'
user        => {...}
```

If you want to see more complete examples, click [here](../master/examples)

#### Authorization
------------------
Get access_token using buffer [docs](https://bufferapp.com/developers/api/oauth)

```python

service = AuthService(client_id, client_secret, redirect_uri)

url = service.authorize_url

# Access the url and retrieve the token
auth_code = #Paste the code from the redirected url

access_token = service.get_access_token(auth_code)

api = service.create_session(access_token)
```

#### User
----------
A user represents a single Buffer user account.

```python

api = API(client_id='client_id',
          client_secret='client_secret',
          access_token='access_token')

# instantiate an user object
user = User(api=api)

print user
print user.id
print user.timezone
```

#### Profile
------------
A Buffer profile represents a connection to a single social media account.

```python
profiles = Profiles(api=api)
print profiles.all() # get all profiles

# filter profiles using some criteria
profile = Profiles(api=api).filter(service='twitter')[0]
print profile # my twitter profile

# get schedules of my twitter profile
print profile.schedules

# update schedules times for my twitter profile
profile.schedules = {
  'days': ['tue', 'thu'],
  'times': ['13:45']
}
```

#### Update
-----------
An update represents a single post to a single social media account.

```python
# retrieve a single update based on an id
update = Update(api=api, id='51de8d33e48c051712000019')
print update

# get update's interactions
print update.interactions

# edit
update = update.edit(text="Hey!")

# publish now
update.publish()

# move to top
update.move_to_top()

# delete
update.delete()
```

#### Updates and profiles
-------------------------

```python
# get all pending updates of a social network profile
profile = Profiles(api=api).filter(service='twitter')[0]
print profile.updates.pending

# get all sent updates of a social network profile
print profile.updates.sent

# retrieve all update's interactions
print profile.updates.sent[0].interactions

# shuffle updates
print profile.updates.shuffle(count=10)

# reorder updates
print profile.updates.reorder(['51dd27629f7fdf520d00009a'])

# create an update
print profile.updates.new("Hello there", now=True)
```

#### Links
----------
A link represents a unique URL that has been shared through Buffer

```python
# get a link's shares
print Link(api=api, url='http%3A%2F%2Fbufferapp.com').shares
```

#### Info
---------
Returns an object with the current configuration that Buffer is using,
including supported services, their icons and the varying limits of character 
and schedules.

```python
# instantiate the api object
api = API(client_id='client_id',
          client_secret='client_secret',
          access_token='access_token')

# get api's info
print api.info
```
