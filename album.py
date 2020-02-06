import json
import matplotlib.pyplot as plt
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
except error:
    print("Cannot do")
data = json.loads(r.text)
#print(data)

# Iniciates needed variables
uris = ''
titles = []
danceability = []
energy = []
speechiness = []
acousticness = []
instrumentalness = []
liveness = []
valence = []
features = [danceability,energy,speechiness,acousticness,instrumentalness,liveness,valence]
features_list = ['Danceability','Energy','Speechiness','Acousticness','Instrumentalness','Liveness','Valence']

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

x = []

for n in range(0,len(titles)):
    danceability.append(data['audio_features'][n]['danceability'])
    energy.append(data['audio_features'][n]['energy'])
    speechiness.append(data['audio_features'][n]['speechiness'])
    acousticness.append(data['audio_features'][n]['acousticness'])
    instrumentalness.append(data['audio_features'][n]['instrumentalness'])
    liveness.append(data['audio_features'][n]['liveness'])
    valence.append(data['audio_features'][n]['valence'])

for n in range(0,len(titles)):
    x.append(n+1)
    pass

for n in range(0,len(titles)):
    plt.subplot(2,3,n+1)
    plt.scatter(x,features[n])
    plt.ylim(-0.25,1)
    plt.xlim(0,len(titles)+1)
    plt.title(features_list[n])
    # Etiquette
    #for b in range(0,len(features_list)):
    #    val = features[n]
    #    plt.annotate(features_list[b],((b+1),val[b]))


plt.subplots_adjust(wspace=0.50,hspace=0.75)
plt.savefig('900.png', dpi=300)
