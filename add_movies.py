import os
import json
import requests
from decouple import config

movies = json.load(open("movies.json"))

request_url = config("MOVIE_URL") + "movie" + "?api-key=" + config("MOVIE_API_KEY")

for movie in movies:
    title = movie['title']
    data = json.dumps({
        'title': movie['title'],
        'qualityProfileId': movie['qualityProfileId'],
        'titleSlug': movie['titleSlug'],
        'images': movie['images'],
        'tmdbId': movie['tmdbId'],
        'year': movie['year'],
        'path': movie['path'],
        'monitored': movie['monitored'],
    })
    response = requests.post(url=request_url, data=data)
    if response.status_code is not 201:
        print(f'Failed to add \'{title}\'')
    else:
        print(f'Added \'{title}\'')

