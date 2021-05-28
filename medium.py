import requests
import json
from constants import graph, rest

def get_user(username): # rest
    response = requests.get(rest.GET_USER_URL % username)
    if response.status_code != 200:
        return (False, response)
    response_dict = json.loads(response.text.replace('])}while(1);</x>', '', 1))
    return response_dict['payload']['user']

def get_user_publications(userid): # graphql
    body = {'operationName': graph.publication_operation_name, 'query': graph.publication_query, 'variables': graph.publication_variables % userid}
    headers = {'Content-Type': 'application/json'}
    r = requests.post('https://medium.com/_/graphql', json=body, headers=headers)
    if r.status_code == 200:
        collections = r.json()['data']['userResult']['followingCollectionConnection']['collections']
        return collections

def get_list_of_followings(userid): # rest
    next_id = None
    followings = []
    while True:
        if next_id:     
            # If this is not the first page of the followings list
            url = (rest.GET_FOLLOWING_URL + '?limit=8&to=' + next_id) % userid
        else:
            # If this is the first page of the followings list
            url = rest.GET_FOLLOWING_URL % userid
        response = requests.get(url)
        response_dict = json.loads(response.text.split('])}while(1);</x>')[1])
        payload = response_dict['payload']
        for user in payload['value']:
            followings.append(user)
        try:            
            next_id = payload['paging']['next']['to']        
        except:
            break
    return followings

def get_list_of_followers(userid): # rest
    next_id = None
    followers = []
    while True:
        if next_id:     
            # If this is not the first page of the followers list
            url = (rest.GET_FOLLOWERS_URL + '?limit=8&to=' + next_id) % userid
        else:
            # If this is the first page of the followers list
            url = rest.GET_FOLLOWERS_URL % userid
        response = requests.get(url)
        response_dict = json.loads(response.text.split('])}while(1);</x>')[1])
        payload = response_dict['payload']
        for user in payload['value']:
            followers.append(user)
        try:
            next_id = payload['paging']['next']['to']    
        except:
            break
    return followers
