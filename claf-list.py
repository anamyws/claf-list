import requests
from time import time
from hashlib import md5
from user_agent import generate_user_agent
from random import randrange
from threading import Thread
def get_id():
  return str(randrange(10000, 18249515))
def get_username():
  id=get_id()
  while True:
    try:
      csrftoken = md5(str(time()).encode()).hexdigest()
      headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'dpr': '0.8',
    'origin': 'https://www.instagram.com',
    'user-agent': generate_user_agent(),
    'x-csrftoken': csrftoken,
    }
      data = {
    '__spin_b': 'trunk',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
    'variables': '{"userID":"'+id+'","username":"0s9s"}',
    'server_timestamps': 'true',
    'doc_id': '7666785636679494',
}
      response = requests.post('https://www.instagram.com/graphql/query', headers=headers, data=data).json()
      username=response['data']['user']['username']
      print(username+' from '+id)
      with open('ass.txt', 'a') as f:
        f.write(username + '\n')
    except:
      print('error get username',id)
for i in range(100):
  Thread(target=get_username).start()