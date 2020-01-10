# Small sonarr and radarr api programs 
### Usage:
Create a .env file with the following parameters:
```
MOVIE_API_KEY = "your radarr api key"
MOVIE_URL = "http://radarr.example.com/api/"
SERIES_API_KEY = "your sonarr api key"
SERIES_URL = "http://sonarr.example.com/api/"
```
Install python packages  
`pip3 install -r requirements.txt`  
Run the program of your choice  
`python3 download_movie_json.py`

### Program descriptions
`download_movie_json.py` Creates a json-file called `movies.json` containing the get response data from /api/movie  
`download_series_json.py` Creates a json-file called `series.json` containing the get response data from /api/series  
`add_movies.py` Adds movies to radarr from `movies.json` using post requests to /api/movie  
`add_series.py` Adds series to sonarr from `series.json` using post requests to /api/series

I created these programs to be used for when I reset my server but want to keep all of my movies and series data.