# Movie Trailer Website

Source code for a Movie Trailer website.

## Overview

This repository contains Python source code for generating a website that displays movie posters and their titles. Each movie tile can be clicked to watch the trailer for that movie.

## Requirements

- You need to have Python installed on your system to run the script.
- You also need to have a [TMDb](https://www.themoviedb.org/) account and your API key which you can get [here](https://developers.themoviedb.org/3/getting-started/introduction).
- Finally, you need to have an internet connection to be able to watch the trailers.

### Installation of Python

If you don't have Python installed on your system already, you can download it [here](https://www.python.org/downloads/).

## How to run

Follow these steps to generate the movie trailer website:

- Navigate to the directory in which these Python modules are present by using `cd` command.
- Make sure to change the line `API_KEY = 'YOUR_API_KEY_HERE'` in `media.py` by replacing `YOUR_API_KEY_HERE` by your own API key.
- (optional) If you want to generate your own movie tiles, then you'll need to get their IDs by searching for the movie on [TMDb](https://www.themoviedb.org/) and getting its ID. Then make suitable changes to `entertainment_center.py` file, while seeding IDs for your own choice of movies.
- Now, run `entertainment_center.py` like this:

    ``` bash
    python entertainment_center.py
    ```
  or
    ``` bash
    python3 entertainment_center.py
    ```

### Credits

This project is powered by [TMDB's](https://www.themoviedb.org/) API.

### Contributors

The starter code for this project was provided by [Udacity](https://github.com/udacity) and the rest of the development has been done by [Mohit Sakhuja](https://github.com/mohitsakhuja).
