import csv
import json

from pprint import pprint as pp

from data.films_data import films, films_title
from utils.films_agr import agregate_directors

import pandas

directors = agregate_directors(films)
print(directors)

exit()
# directors = agregate_budget()
# print(directors)

# user_choise = input("Choose film: ")


# def search_film_by_title(films, query):
#     for film in films:
#         if user_choise == film['title']:
#             return list(film.items())
        
#     return "Такого фільму немає в нашій базі"


# def count_budget():
#     pass

# result = search_film_by_title(films_data.films, user_choise)

# if type(result) == list:
#     for key, val in result:
#         print(key, val, sep=": ")
# else:
#     print(result)
