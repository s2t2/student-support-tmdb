import os
import json

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("API_KEY")

# inferring these from https://developers.themoviedb.org/3/genres/get-movie-list
genre_list = ["action", "adventure", "documentary", "horror", "mystery", "science fiction"]
print("GENRES:", genre_list)

# supplied by MC on 4/22...


# NEED TO IMPORT THE API KEYS FOR TMDB AND ROTTEN TOMATOES


# CREATE USER INPUT FOR GENRE AND YEAR OF MOVIE

number_of_movies = 85000



while True:
    genre_input = input("Enter the name of the genre you want: ")
    if genre_input.lower() in genre_list:

        for collection in range(number_of_movies):
            request_url = "https://api.themoviedb.org/3/movie/" + str(collection) + f"?api_key={API_KEY}"
            print(request_url)
            data = requests.get(request_url)

            if data.status_code == 200:
                json_string = data.text
                obj = json.loads(json_string)

                for ele in obj['genres']:
                    if genre_input == ele['name'].lower():
                        print(obj['original_title'])

            # GOT CODE FROM STACK OVERFLOW
    else:
        print("Please make sure to enter a valid genre")

        if "Error" in data.text:
            print("The genre you are looking for is not here")
        else:
            break

    # GOT SOME OF THIS CODE FROM THE ROBO ADVISOR PROJECT

# PULL DATA FROM TMDB AND ROTTEN TOMATOES W MATCHING GENRE/YEAR



# OUTPUT THREE RECOM
