import requests
import json
from pprint import pprint


def get_film_by_keyword(keyword):
    url = f"https://moviesminidatabase.p.rapidapi.com/movie/imdb_id/byTitle/{keyword}/"
    
    headers = {
		"X-RapidAPI-Key": "2cbe1506f2msh8afa3a8d1441a0ep1fd5b0jsn32e39521aff9",
		"X-RapidAPI-Host": "moviesminidatabase.p.rapidapi.com"
	}
    response = requests.get(url, headers=headers)
    
    return response.json()

data = get_film_by_keyword("love")

file_obj = open('data.json', 'w')
json.dump(data, file_obj)