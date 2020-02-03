import json
import matplotlib as plt
import requests

id = '3yj1EziuVuch1OayyM95az'
url = 'https://api.spotify.com/v1/albums/{}/tracks'
headers = {'Authorization':'Bearer {}'}

abulm = requests.get('https://api.spotify.com/v1/albums/{}/tracks'.format(id),headers=headers)
song = requests.get('https://api.spotify.com/v1/audio-features/{}',headers=headers)
data = json.loads(abulm.text)
uris = []
song_titles = []

# Get songs from album

for n in range(1,len(data)):
    uri = data['items'][n]['uri']
    uri = uri[14:len(uri)]
    uris.append(uri)
    song_titles.append(data['items'][n]['name'])
print(uris)

# Get song features
for n in range (0,len(uris)):
    song  = requests.get('https://api.spotify.com/v1/audio-features/{}'.format(uris[n]),headers=headers)
    #print(song.text)
    # Loads data into the fixed structure below for every song
    features = json.loads(song.text)
    features_clean = [{'name':'danceability','value':0},{'name':'energy','value':0},{'name':'speechiness','value':0},{'name':'acousticness','value':0},{'name':'instrumentalness','value':0},{'name':'liveness','value':0},{'name':'valence','value':0}]
 
    for n in range(0,len(features_clean)):
        print(features[features_clean[n]['name']])
        features_clean[n]['value'] = features[features_clean[n]['name']]
    album[n]['features'] = features_clean
 
    print(features_clean)




