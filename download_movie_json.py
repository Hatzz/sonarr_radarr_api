import os
import json
import requests
from decouple import config

request_url = config("MOVIE_URL") + "movie" + "?api-key=" + config("MOVIE_API_KEY")
response = requests.get(url=request_url)
with open("movies.json", "w") as json_file:
    json.dump(response.json(), json_file)