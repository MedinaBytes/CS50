from flask import Flask, render_template, request
import requests
import random
from datetime import datetime

app = Flask(__name__)

# Your TMDb API key
API_KEY = "f4e25af08ed4c18a043e3ffa3ae42d28"
BASE_URL = "https://api.themoviedb.org/3"

# Genre Mapping (ID from TMDb API)
GENRE_IDS_MOVIE = {
    'Action': 28,
    'Comedy': 35,
    'Drama': 18,
    'Horror': 27,
    'Romance': 10749,
    'Sci-Fi': 878
}

GENRE_IDS_TV = {
    'Action': 10759,
    'Comedy': 35,
    'Drama': 18,
    'Horror': 27,
    'Romance': 10749,
    'Sci-Fi': 10765
}

def get_genre_names(genre_ids, movie_type):
    genre_url = f"{BASE_URL}/genre/{'movie' if movie_type == 'movie' else 'tv'}/list"
    response = requests.get(genre_url, params={'api_key': API_KEY})
    genres_data = response.json().get('genres', [])
    genre_dict = {str(genre['id']): genre['name'] for genre in genres_data}
    return [genre_dict.get(str(genre_id)) for genre_id in genre_ids if genre_dict.get(str(genre_id))]

def get_trailer_url(movie_id, movie_type):
    video_url = f"{BASE_URL}/{'movie' if movie_type == 'movie' else 'tv'}/{movie_id}/videos"
    response = requests.get(video_url, params={'api_key': API_KEY})
    videos = response.json().get('results', [])
    trailer = next((video for video in videos if video['type'] == 'Trailer'), None)
    if trailer:
        return f"https://www.youtube.com/watch?v={trailer['key']}"
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Romance', 'Sci-Fi']
    current_year = datetime.now().year
    years = range(current_year, 1900, -1)  # Descending order

    # Get user filter inputs
    genre = request.form.get('genre', '')
    year = request.form.get('year', str(current_year))
    movie_type = request.form.get('type', 'movie')

    if movie_type == 'movie':
        url = f"{BASE_URL}/discover/movie"
        genre_mapping = GENRE_IDS_MOVIE
    else:
        url = f"{BASE_URL}/discover/tv"
        genre_mapping = GENRE_IDS_TV

    params = {
        'api_key': API_KEY,
        'language': 'en-US',
        'sort_by': 'popularity.desc',
        'page': 1
    }

    if genre:
        genre_id = genre_mapping.get(genre)
        if genre_id:
            params['with_genres'] = genre_id

    if year:
        params['primary_release_year' if movie_type == 'movie' else 'first_air_date_year'] = year

    try:
        response = requests.get(url, params=params)
        data = response.json()
        all_movies = data.get('results', [])

        if len(all_movies) > 5:
            selected_movies = random.sample(all_movies, 5)
        else:
            selected_movies = all_movies[:5]

        main_movie = selected_movies[0] if selected_movies else None

        # Enhanced movie data
        if main_movie:
            movie_id = main_movie['id']

            # Get genres
            main_movie['genre_names'] = get_genre_names(main_movie.get('genre_ids', []), movie_type)

            # Get trailer
            main_movie['trailer_url'] = get_trailer_url(movie_id, movie_type)

            # Get cast
            credit_url = f"{BASE_URL}/{'movie' if movie_type == 'movie' else 'tv'}/{movie_id}/credits"
            credit_response = requests.get(credit_url, params={'api_key': API_KEY})
            credit_data = credit_response.json()
            actors = [actor['name'] for actor in credit_data.get('cast', [])[:5]]

            # Add additional data to suggestion movies
            for movie in selected_movies[1:]:
                movie['genre_names'] = get_genre_names(movie.get('genre_ids', []), movie_type)
                movie['trailer_url'] = get_trailer_url(movie['id'], movie_type)

        else:
            actors = []

    except Exception as e:
        print(f"Error fetching data: {e}")
        selected_movies = []
        main_movie = None
        actors = []

    return render_template(
        "index.html",
        movie=main_movie,
        movies=selected_movies[1:] if selected_movies else [],
        genres=genres,
        years=years,
        movie_type=movie_type,
        actors=actors
    )

if __name__ == '__main__':
    app.run(debug=True)
