""" Module that contains the necessary functions for
    entertainment.py
"""

import requests

# Private API_KEY
API_KEY = "YOUR_API_KEY_HERE"

# To get video data
APPEND = "&append_to_response=videos"


class Movie():
    """A class that represents a movie and contains information
        about it.
    """

    def __init__(self, movie_id):
        """Initialize the movie object."""
        temp_dict = create_movie_dict(movie_id)
        self.title = temp_dict['title']
        self.storyline = temp_dict['storyline']
        self.poster_image_url = temp_dict['poster_image_url']
        self.trailer_youtube_url = temp_dict['trailer_youtube_url']


def create_movie_dict(movie_id):
    """
        Creates a dictionary containing values for
        title, storyline, poster_url and youtube_trailer_url.
    """

    # String to send to the server
    movie_string = "https://api.themoviedb.org/3/movie/"
    movie_string += str(movie_id) + "?api_key=" + API_KEY + APPEND

    # Send a request
    try:
        data = requests.get(movie_string)
    except ConnectionError:
        return None

    # Convert to a dictionary
    try:
        response = data.json()
    except ValueError:
        return None

    # Return a dictionary
    try:
        return {
            "title": response['title'],
            "storyline": response['overview'],
            "poster_image_url": "https://image.tmdb.org/t/p/w500/" +
                                response['poster_path'],
            "trailer_youtube_url": "https://www.youtube.com/watch?v=" +
                                response['videos']['results'][0]['key']
        }
    except KeyError:
        return None
