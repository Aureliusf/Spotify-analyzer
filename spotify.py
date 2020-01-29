import json
import requests
#with open('1.json', 'r') as json_file:
#    data = json.load(json_file)
#print(data)

id = 'GVZn2EmQiJNzWPvOm7dt'

url = 'https://api.spotify.com/v1/audio-features/{}'
headers = {'Authorization':'Bearer BQA8eQvzCH4GuAKKgiAVX7-UmFvgcG-C-xIxe28XCTLnKqtvvHg0wowfv6Gb1lwgn0_6zd4sQ_8KJgw5bCRJxU0Qu1cIBoeY_p1uhrhk8O0b71dKl4cBteQMOtBn9l7-ZpXVEMmKFgasung'}

r = requests.get(url.format(id),headers=headers)

print(r.text)


