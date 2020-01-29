import json
import requests
id = []
id.append('4V3PsyJJOVXw1SNm7pJh6e')
id.append('3yj1EziuVuch1OayyM95az')
url = 'https://api.spotify.com/v1/audio-features/{}'
headers = {'Authorization':'Bearer {}'}

song = requests.get('https://api.spotify.com/v1/audio-features/{}'.format(id[0]),headers=headers)

print(song.text)


