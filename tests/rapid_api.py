import requests
from pprint import pprint

url = """https://moviesminidatabase.p.rapidapi.com/movie/imdb_id/byTitle/Die%20Hard/"""

headers = {
	"X-RapidAPI-Key": "2cbe1506f2msh8afa3a8d1441a0ep1fd5b0jsn32e39521aff9",
	"X-RapidAPI-Host": "moviesminidatabase.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

pprint(response.json())
