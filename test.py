import json
import requests
id = []
id.append('4V3PsyJJOVXw1SNm7pJh6e')
id.append('3yj1EziuVuch1OayyM95az')
url = 'https://api.spotify.com/v1/audio-features/{}'
headers = {'Authorization':'Bearer BQA8eQvzCH4GuAKKgiAVX7-UmFvgcG-C-xIxe28XCTLnKqtvvHg0wowfv6Gb1lwgn0_6zd4sQ_8KJgw5bCRJxU0Qu1cIBoeY_p1uhrhk8O0b71dKl4cBteQMOtBn9l7-ZpXVEMmKFgasung'}

song = requests.get('https://api.spotify.com/v1/audio-features/{}'.format(id[0]),headers=headers)

print(song.text)


