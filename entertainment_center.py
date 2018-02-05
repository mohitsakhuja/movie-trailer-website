"""
    Script for creating movie objects
    and displaying movie posters on a webbrowser
    that link to their respective trailers on YouTube
"""

from media import Movie
from fresh_tomatoes import open_movies_page

# Create an empty list to hold the movies
movies = []

# Make movie objects
interstellar = Movie(157336)
movies.append(interstellar)

easy_a = Movie(37735)
movies.append(easy_a)

doctor_strange = Movie(284052)
movies.append(doctor_strange)

the_dark_knight = Movie(155)
movies.append(the_dark_knight)

the_godfather = Movie(238)
movies.append(the_godfather)

civil_war = Movie(271110)
movies.append(civil_war)

# Open website
open_movies_page(movies)
