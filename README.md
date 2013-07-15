buffer-app-python (buffpy)
==========================
Simple to use python library for Buffer App

### ORM`ish
------------
Bufferapp.com expose some usefull entities:
  * user
  * profile
  * update
  * link
  * info

Every entity can be seen as an object that have attributes and methods. Those
methdos and attributes are linked to some endpoints.

All those objects are special dicts. You can do something like
```python
user.id     => '12455678976asd'
user        => {...}
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
A Buffer profile represents a connection to a single social media account.

```python
profiles = Profiles(api=api)
print profiles.all() # get all profiles

# filter profiles using some criteria
profile = Profiles(api=api).filter(service='twitter')[0]
print profile # my twitter profile

# get schedules of my twitter profile
profile = Profiles(api=api).filter(service='twitter')[0]
print profile.schedules

# update schedules times for my twitter profile
profile = Profiles(api=api).filter(service='twitter')[0]

profile.schedules = {
  'days': ['tue', 'thu'],
  'times': ['13:45']
}
```
