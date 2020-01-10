import json
import requests
from decouple import config

request_url = config("SERIES_URL") + "series" + "?api-key=" + config("SERIES_API_KEY")
response = requests.get(url=request_url)
with open("series.json", "w") as json_file:
    json.dump(response.json(), json_file)