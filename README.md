# medium-python
A Python wrapper for the medium private API

# Installation:
```
git clone https://github.com/erfanhs/medium_private_api.git
cd medium_private_api
pip3 install -r requirements.txt
```

# Usage:
```python
from medium import get_user, get_user_publications, get_list_of_followings, get_list_of_followers

username = 'erfanharirsaz071'

# get user json
user = get_user(username)

# get user publications
publications = get_user_publications(user['userId'])
for pub in publications:
    print(pub['name'], pub['slug'], pub['id'])

# get user followings
followings = get_list_of_followings(user['userId'])
for u in followings:
    print(u['username'])
    
# get user followers
followers = get_list_of_followers(user['userId'])
for u in followers:
    print(u['username'])
```
