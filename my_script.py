import os
import json

import requests
from dotenv import load_dotenv

load_dotenv()

#API_KEY = os.environ.get("API_KEY")
API_KEY_V3 = os.environ.get("API_KEY_V3")
API_KEY_v4 = os.environ.get("API_KEY_V4")

# inferring these from https://developers.themoviedb.org/3/genres/get-movie-list
genre_list = ["action", "adventure", "documentary", "horror", "mystery", "science fiction"]
print("GENRES:", genre_list)

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

number_of_requests = 25
number_of_movies = 3

matching_movies = []


# simplifying this for now...

genre_input = "documentary" # input("Enter the name of the genre you want: ")
print("SELECTED GENRE:", genre_input)
if genre_input.lower() in genre_list:

    while len(matching_movies) <= number_of_movies:

        for movie_id in range(number_of_requests):
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

            if "Error" in data.text:
                print("The genre you are looking for is not here")
                exit()

else:
    print("Please make sure to enter a valid genre")
    exit()

print("-------------------")
print("MATCHING MOVIES:")
for matching_movie in matching_movies:
    print(type(matching_movie), matching_movie)
