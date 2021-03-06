import os
import json
import pprint as pp # see: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/pprint.md
import random

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY_V3 = os.environ.get("API_KEY_V3")

#
# USER SELECTS GENRE
#

# inferring these from https://developers.themoviedb.org/3/genres/get-movie-list
genre_list = ["action", "adventure", "documentary", "horror", "mystery", "science fiction"]
print("GENRES:", genre_list)

genre_input = "documentary" # input("Enter the name of the genre you want: ")
print("SELECTED GENRE:", genre_input)

# h/t: https://www.themoviedb.org/talk/59fcec1fc3a368689300071d?language=en-US

genre_id = 28 # todo: lookup id matching the selected genre (see genres.json or make a request to https://developers.themoviedb.org/3/genres/get-movie-list):

request_url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY_V3}&language=en-US&sort_by=popularity.desc&with_genres={genre_id}"
print(request_url)
data = requests.get(request_url)

if data.status_code == 200:
    json_string = data.text
    parsed_response = json.loads(json_string)

    #breakpoint()
    # (Pdb) type(parsed_response)
    # <class 'dict'>
    # (Pdb) parsed_response.keys()
    # dict_keys(['page', 'total_results', 'total_pages', 'results'])

    matching_movies = parsed_response["results"]

    print(type(matching_movies))
    print("-------------------")
    print("MATCHING MOVIES:")
    for matching_movie in matching_movies:
        pp.pprint(matching_movie)
        print("---------")
