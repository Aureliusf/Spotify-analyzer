import json
import requests
#with open('1.json', 'r') as json_file:
#    data = json.load(json_file)
#print(data)

id = 'GVZn2EmQiJNzWPvOm7dt'

url = 'https://api.spotify.com/v1/audio-features/{}'
headers = {'Authorization':'Bearer {}'}

r = requests.get(url.format(id),headers=headers)

print(r.text)


