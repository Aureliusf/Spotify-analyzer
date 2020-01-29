import json
import requests

id = '3yj1EziuVuch1OayyM95az'
url = 'https://api.spotify.com/v1/albums/{}/tracks'
headers = {'Authorization':'Bearer BQA8eQvzCH4GuAKKgiAVX7-UmFvgcG-C-xIxe28XCTLnKqtvvHg0wowfv6Gb1lwgn0_6zd4sQ_8KJgw5bCRJxU0Qu1cIBoeY_p1uhrhk8O0b71dKl4cBteQMOtBn9l7-ZpXVEMmKFgasung'}

abulm = requests.get('https://api.spotify.com/v1/albums/{}/tracks'.format(id),headers=headers)
data = json.loads(abulm.text)
uris = []
song_titles = []


danceability = []
energy = []
key = []
loudness = []
mode = []
speechiness = []
acousticness = []
instrumentalness = []
liveness = []
valence = []
tempo = []
duration_ms = []



# Get songs from album

for n in range(1,len(data['items'])):
    uri = data['items'][n]['uri']
    uri = uri[14:len(uri)]
    uris.append(uri)
    song_titles.append(data['items'][n]['name'])
print(uris)

# Get songs stats
for n in range(1,len(uris)):
    id = uris[n]
    #print(uris[n])
    analisis = json.loads(requests.get('https://api.spotify.com/v1/audio-features/{}'.format(id),headers=headers).text)
    print(analisis["danceability"])
	danceability.append(analisis["danceability"])
	energy.append(analisis['energy'])
	key.append(analisis['key'])
	loudness.append(analisis['loudness'])
	mode.append(analisis['mode'])
	speechiness.append(analisis['speechiness'])
	acousticness.append(analisis['acousticness'])
	instrumentalness.append(analisis['instrumentalness'])
	liveness.append(analisis['liveness'])
	valence.append(analisis['valence'])
	tempo.append(analisis['tempo'])
	duration_ms.append(analisis['duration_ms'])

print(song_titles[1],danceability[1])
