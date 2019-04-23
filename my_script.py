import os
import json
import pprint as pp # see: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/pprint.md
import random

import requests
from dotenv import load_dotenv

load_dotenv()

#API_KEY = os.environ.get("API_KEY")
API_KEY_V3 = os.environ.get("API_KEY_V3")
API_KEY_v4 = os.environ.get("API_KEY_V4")

#
# USER SELECTS GENRE
#

# inferring these from https://developers.themoviedb.org/3/genres/get-movie-list
genre_list = ["action", "adventure", "documentary", "horror", "mystery", "science fiction"]
print("GENRES:", genre_list)

genre_input = "documentary" # input("Enter the name of the genre you want: ")
print("SELECTED GENRE:", genre_input)


# prefer to issue a single request
# researching:
#  + https://developers.themoviedb.org/3/movies/get-movie-details
#  + https://developers.themoviedb.org/3/genres/get-movie-list
#  + https://www.themoviedb.org/documentation/api/discover
#  + https://www.themoviedb.org/documentation/api/wrappers-libraries
#  + https://github.com/celiao/tmdbsimple/
#  + https://github.com/wagnerrp/pytmdb3/
#  + https://www.themoviedb.org/discover/movie
#  + https://developers.themoviedb.org/4/getting-started/authorization
# not finding anything that jumps out. will need to do more research.
# in the meantime, here's how to get three movies and choose at random...

#
# REQUEST(S) FOR MATCHING MOVIES
#

number_of_movies_available = 85000 # does this number come from somewhere? hopefully we can find documentation on the number of available movies, but this will probably change over time, and its another reason to prefer a different approach
movie_ids = list(range(number_of_movies_available)) # makes a list from 1 to this number
random.shuffle(movie_ids) # sort randomly, which will introduce randomness into the request process. see: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/random.md
print("SOME RANDOM MOVIE IDS:", movie_ids[0:25])

matching_movies = []
desired_number_of_matching_movies = 3

for movie_id in movie_ids:
    if len(matching_movies) <= desired_number_of_matching_movies:

        request_url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + f"?api_key={API_KEY_V3}"
        print(request_url)
        data = requests.get(request_url)

        if data.status_code == 200:
            json_string = data.text
            movie = json.loads(json_string)

            for genre in movie['genres']:
                if genre_input == genre['name'].lower():
                    print(movie['original_title'])
                    matching_movies.append(movie)

    else:
        print("OH, FOUND THE DESIRED NUMBER OF MATCHING MOVIES...")
        break # avoids attempts to continue requesting movies


print("-------------------")
print("MATCHING MOVIES:")
for matching_movie in matching_movies:
    pp.pprint(matching_movie)
    print("---------")
