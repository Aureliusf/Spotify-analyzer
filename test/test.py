import json
import requests
import matplotlib.pyplot as plt

# Reads API key, this solution is temporary and really messy
try:
    with open("temp-key.txt", "r") as f:
        api_key = f.read().strip()
except FileNotFoundError:
    print("File not found")
#print(api_key)

id = []
id.append('4V3PsyJJOVXw1SNm7pJh6e')
id.append('3yj1EziuVuch1OayyM95az')
url = 'https://api.spotify.com/v1/audio-features/{}'
headers = {'Authorization':'Bearer {}'.format(api_key)}

song = requests.get('https://api.spotify.com/v1/audio-features/{}'.format(id[0]),headers=headers)

#print(song.text)

# Loads data into the fixed structure below
features = json.loads(song.text)
features_clean = [{'name':'danceability','value':0},{'name':'energy','value':0},{'name':'speechiness','value':0},{'name':'acousticness','value':0},{'name':'instrumentalness','value':0},{'name':'liveness','value':0},{'name':'valence','value':0}]

for n in range(0,len(features_clean)):
    print(features[features_clean[n]['name']])
    features_clean[n]['value'] = features[features_clean[n]['name']]

#print(features_clean)


# Title compose
values = []
for n in range(0,len(features_clean)):
    values.append(features_clean[n]['value'])
max_index = values.index(max(values))
title = 'This song is big on {}'

# Plotting
x = [1,2,3,4,5,6,7]
y = [features_clean[0]['value'],features_clean[1]['value'],features_clean[2]['value'],features_clean[3]['value'],features_clean[4]['value'],features_clean[5]['value'],features_clean[6]['value']]

plt.scatter(x,y,s=30)
plt.title(title.format(features_clean[max_index]['name']))
plt.ylim(top=1)

    # Annotation system, i know its a bad
for n in range(0,len(features_clean)):
    plt.annotate(features_clean[n]['name'],((n+1),features_clean[n]['value']))

plt.show()
