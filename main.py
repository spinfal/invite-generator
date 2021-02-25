import requests as r
import time as t
import random
import string

# 7 - <12 hrs
# 8 - 24 hrs
# 9 - idk threw it in here
# 10 - permanent

channel = input('channel id: ')
token = input('token: ')

while True:
  def invGen(size=random.randrange(7,10), chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
    
  invCode = f'discord.gg/{invGen()}'
  
  url = f'https://discordapp.com/api/v8/channels/{channel}/messages'

  headers = {
    'Content-type': 'application/json',
    'Authorization': token,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
  }

  json = {
    'content': invCode
  }

  res = r.post(url, headers=headers, json=json)
  
  print(f'status: {str(res.status_code)}\ncode: {invCode}')
  
  if res.status_code == 429:
    print('\nratelimted... please wait...\n')
    t.sleep(9)