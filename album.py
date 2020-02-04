import json
import matplotlib as plt
import requests

# Reads API key, this solution is temporary and really messy
try:
    with open("temp-key.txt", "r") as f:
        api_key = f.read().strip()
except FileNotFoundError:
    print("File not found")
#print(api_key)

# Set album id, headers and requests
id = '3yj1EziuVuch1OayyM95az'
headers = {'Authorization':'Bearer {}'.format(api_key)}
try:
    r = requests.get('https://api.spotify.com/v1/albums/{}/tracks'.format(id),headers=headers)
except NoResponse:
    print("Cannot do")
data = json.loads(r.text)
#print(data)

# Iniciates needed variables
uris = ''
titles = []

# Get songs from album
for n in range(1,len(data)):
    uri = data['items'][n]['uri']
    titles.append(data['items'][n]['name'])
    uri = uri[14:len(uri)]
    uris = uris+uri+'%2C'
#print(uris)

# Get songs features
try:
    r = requests.get('https://api.spotify.com/v1/audio-features?ids={}'.format(uris),headers=headers)
except NoResponse:
    print('Cannot do')

data = json.loads(r.text)

for n in range(0,len(titles)):
    print(data['audio_features'][n]['id'],titles[n])
