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
print('Which album do you want to analyze, please paste the uri here:')
id = input()
headers = {'Authorization':'Bearer {}'.format(api_key)}
try:
    r = requests.get('https://api.spotify.com/v1/albums/{}/tracks?limit=50'.format(id),headers=headers)
except error:
    print("Cannot do")
data = json.loads(r.text)
#print(data)
#print(len(data['items']))

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
bestest = []

# Get songs from album
for n in range(0,len(data['items'])):
    uri = data['items'][n]['uri']
    titles.append(data['items'][n]['name'])
    uri = uri[14:len(uri)]
    uris = uris+uri+'%2C'
#print(uris)
#print(len(titles))

# Get songs features
try:
    r = requests.get('https://api.spotify.com/v1/audio-features?ids={}'.format(uris),headers=headers)
except NoResponse:
    print('Cannot do')

data = json.loads(r.text)
#print(len(data['audio_features']))

x = []

for n in range(0,len(titles)):
    danceability.append(data['audio_features'][n]['danceability'])
    energy.append(data['audio_features'][n]['energy'])
    speechiness.append(data['audio_features'][n]['speechiness'])
    acousticness.append(data['audio_features'][n]['acousticness'])
    instrumentalness.append(data['audio_features'][n]['instrumentalness'])
    liveness.append(data['audio_features'][n]['liveness'])
    valence.append(data['audio_features'][n]['valence'])

# Creating X axis for corresponding size
for n in range(0,len(titles)):
    x.append(n+1)

for n in range(0,7):
    value =[]
    most =0
    for b in range(0,len(features[n])):
        value.append(features[n][b])
    most = value.index(max(value))
    bestest.append(titles[most])

# Plotting
for n in range(0,len(features)):
    plt.subplot(4,3,n+1)
    #Color Etiquette
    for b in range(0,len(titles)-1):
        plt.scatter(x[b],features[n][b],label=titles[b],s=12)

    plt.ylim(-0.25,1)
    plt.xlim(0,len(titles)+1)
    plt.title('{} \n {}'.format(features_list[n],bestest[n]), fontsize=7)

ncol = int( len(titles)/4)
# Legend
plt.legend(loc = (-0.3, -2.35), ncol=ncol )

plt.subplots_adjust(wspace=0.50,hspace=0.85)
plt.show()
plt.savefig('album.png', dpi=300)
