import json
import matplotlib.pyplot as plt
import requests

# Reads API key, this solution is temporary and really messy
def dance():
    try:
        with open("temp-key.txt", "r") as f:
            api_key = f.read().strip()
    except FileNotFoundError:
        print("File not found")
    #print(api_key)
    return api_key

# Ask for or sets album uri id
def album_id():
    print('Which album do you want to analyze, please paste the uri here:')
    id = input()
    #id = '4aawyAB9vmqN3uQ7FjRGTy'
    return id

# Set headers
def header(api_key):
    headers = {'Authorization':'Bearer {}'.format(api_key)}
    return headers

# Does request
def get_data(id,api_key,headers):
    try:
        r = requests.get('https://api.spotify.com/v1/albums/{}/tracks?limit=50'.format(id),headers=headers)
    except error:
        print("Cannot do")
    data = json.loads(r.text)
    #print(data)
    #print(len(data['items']))
    return data


# Get songs from album
def get_songs(data,titles,uris):
    for n in range(0,len(data['items'])):
        uri = data['items'][n]['uri']
        titles.append(data['items'][n]['name'])
        uri = uri[14:len(uri)]
        uris = uris+uri+'%2C'
        #print(uris)
        #print(len(titles))
    return uris,titles

# Get songs features
def get_features(uris,headers):
    try:
        r = requests.get('https://api.spotify.com/v1/audio-features?ids={}'.format(uris),headers=headers)
    except NoResponse:
        print('Cannot do')
    data = json.loads(r.text)
    #print(len(data['audio_features']))
    return data

# Fetch features in each list
def organize_features(data,titles,danceability,energy,speechiness,acousticness,instrumentalness,liveness,valence):
    features =[]
    for n in range(0,len(titles)):
        danceability.append(data['audio_features'][n]['danceability'])
        energy.append(data['audio_features'][n]['energy'])
        speechiness.append(data['audio_features'][n]['speechiness'])
        acousticness.append(data['audio_features'][n]['acousticness'])
        instrumentalness.append(data['audio_features'][n]['instrumentalness'])
        liveness.append(data['audio_features'][n]['liveness'])
        valence.append(data['audio_features'][n]['valence'])
    features.append(danceability)
    features.append(energy)
    features.append(speechiness)
    features.append(acousticness)
    features.append(instrumentalness)
    features.append(liveness)
    features.append(valence)
    return features

x = []
# Creating X axis for corresponding size
def x_axis(x,titles):
    for n in range(0,len(titles)):
        x.append(n+1)
    return x

# Find max values for each feature
def max_val(features,titles,bestest):
    for n in range(0,7):
        value =[]
        most =0
        for b in range(0,len(features[n])):
            value.append(features[n][b])
        most = value.index(max(value))
        bestest.append(titles[most])
    return bestest

# Plotting
def plot(features,titles,bestest):
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
    plt.legend(loc = (-0.3, -2.35), ncol=ncol , fontsize=7)
    # Padding
    plt.subplots_adjust(wspace=0.50,hspace=0.85)
    # Shows and saves fig to file
    plt.show()
    plt.savefig('album.png', dpi=300)


# Execution

api_key = dance()
id = album_id()
headers = header(api_key)

# Get album data
data = get_data(id,api_key,headers)

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
features_list = ['Danceability','Energy','Speechiness','Acousticness','Instrumentalness','Liveness','Valence']
bestest = []

# Get songs
uris,titles = get_songs(data,titles,uris)

# Get songs data
data = get_features(uris,headers)

# Organize songs features
features = organize_features(data,titles,danceability,energy,speechiness,acousticness,instrumentalness,liveness,valence)

# Find max values for each feature
bestest = max_val(features,titles,bestest)

# Create x axis
x =[]
x = x_axis(x,titles)

# Plotting
plot(features,titles,bestest)
