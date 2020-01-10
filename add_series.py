import os
import json
import requests
from decouple import config

series = json.load(open("series.json"))

request_url = config("SERIES_URL") + "series" + "?api-key=" + config("SERIES_API_KEY")

for serie in series:
    title = serie['title']
    data = json.dumps({
        'tvdbId': serie['tvdbId'],
        'title': serie['title'],
        'profileId': serie['profileId'],
        'titleSlug': serie['titleSlug'],
        'images': serie['images'],
        'seasons': serie['seasons'],
        'seasonFolder': serie['seasonFolder'],
        'monitored': serie['monitored'],
        'path': serie['path'],
    })
    response = requests.post(url=request_url, data=data)
    if response.status_code is not 201:
        print(f'Failed to add \'{title}\'')
        print(response.text)
    else:
        print(f'Added \'{title}\'')
