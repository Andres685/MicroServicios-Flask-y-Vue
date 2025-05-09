from flask_cors import cross_origin
from flask import Blueprint, jsonify, request
import requests
from .config import Config


routes = Blueprint('routes', __name__)


# Endpoint para buscar películas
'''
@routes.route('/movies/search', methods=['GET'])
def search_movies():
    query = request.args.get('query', '')
    page = request.args.get('page', default=1, type=int)
    
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    try:
        response = requests.get(
            f"{TMDB_URL}/search/movie",
            params={
                'api_key': TMDB_API_KEY,
                'query': query,
                'language': 'es-ES',
                'page': page,
                'include_adult': False
            }
        )
        response.raise_for_status()
        
        data = response.json()
        return jsonify({
            'results': data['results'],
            'total_pages': data['total_pages'],
            'total_results': data['total_results'],
            'page': data['page']
        }), 200
        
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para películas populares
@routes.route('/movies/popular', methods=['GET'])
def popular_movies():
    page = request.args.get('page', default=1, type=int)
    
    try:
        response = requests.get(
            f"{TMDB_URL}/movie/popular",
            params={
                'api_key': TMDB_API_KEY,
                'language': 'es-ES',
                'page': page
            }
        )
        response.raise_for_status()
        
        data = response.json()
        return jsonify({
            'results': data['results'],
            'total_pages': data['total_pages'],
            'total_results': data['total_results'],
            'page': data['page']
        }), 200
        
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para detalles de película
@routes.route('/movies/<int:movie_id>', methods=['GET'])
def movie_details(movie_id):
    try:
        # Obtener detalles básicos
        movie_response = requests.get(
            f"{TMDB_URL}/movie/{movie_id}",
            params={
                'api_key': TMDB_API_KEY,
                'language': 'es-ES',
                'append_to_response': 'credits,videos,similar'
            }
        )
        movie_response.raise_for_status()
        movie_data = movie_response.json()

        # Formatear respuesta
        result = {
            'id': movie_data['id'],
            'title': movie_data['title'],
            'overview': movie_data['overview'],
            'poster_path': movie_data['poster_path'],
            'backdrop_path': movie_data['backdrop_path'],
            'release_date': movie_data['release_date'],
            'runtime': movie_data['runtime'],
            'vote_average': movie_data['vote_average'],
            'genres': [g['name'] for g in movie_data['genres']],
            'director': next(
                (p['name'] for p in movie_data['credits']['crew'] if p['job'] == 'Director'),
                'Desconocido'
            ),
            'cast': [
                {
                    'name': actor['name'],
                    'character': actor['character'],
                    'profile_path': actor['profile_path']
                } for actor in movie_data['credits']['cast'][:6]
            ],
            'trailers': [
                {
                    'name': video['name'],
                    'key': video['key'],
                    'type': video['type']
                } for video in movie_data['videos']['results'] 
                if video['site'] == 'YouTube' and video['type'] in ['Trailer', 'Teaser']
            ],
            'similar': [
                {
                    'id': movie['id'],
                    'title': movie['title'],
                    'poster_path': movie['poster_path'],
                    'vote_average': movie['vote_average']
                } for movie in movie_data['similar']['results'][:6]
            ]
        }

        return jsonify(result), 200

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para listar géneros
@routes.route('/genres', methods=['GET'])
def list_genres():
    try:
        response = requests.get(
            f"{TMDB_URL}/genre/movie/list",
            params={
                'api_key': TMDB_API_KEY,
                'language': 'es-ES'
            }
        )
        response.raise_for_status()
        
        return jsonify(response.json()['genres']), 200
        
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para películas por género
@routes.route('/movies/genre/<int:genre_id>', methods=['GET'])
def movies_by_genre(genre_id):
    page = request.args.get('page', default=1, type=int)
    
    try:
        response = requests.get(
            f"{TMDB_URL}/discover/movie",
            params={
                'api_key': TMDB_API_KEY,
                'language': 'es-ES',
                'with_genres': genre_id,
                'page': page,
                'sort_by': 'popularity.desc'
            }
        )
        response.raise_for_status()
        
        data = response.json()
        return jsonify({
            'results': data['results'],
            'total_pages': data['total_pages'],
            'total_results': data['total_results'],
            'page': data['page']
        }), 200
        
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
routes = Blueprint('routes1', __name__)
'''
@routes.route('/api/listar/todo', methods=['POST', 'OPTIONS'])
@cross_origin()
def get_movies_batch():
    """
    Obtiene información de múltiples películas por título
    """
    print("Raw data:", request.data)
    print("JSON:", request.get_json(force=True, silent=True))
    if request.method == 'OPTIONS':
        return '', 200
        
    data = request.get_json()
    titles = data.get('titles')
    
    if not titles or not isinstance(titles, list):
        return jsonify({'message': 'Se requiere una lista de títulos', 'movies': []}), 400
    
    omdb_key = Config.OMDB_API_KEY
    results = []
    
    for title in titles:
        try:
            response = requests.get(f"https://www.omdbapi.com/?apikey={omdb_key}&t={title}")
            movie_data = response.json()
            
            if movie_data.get('Response') == 'True':
                results.append(movie_data)
        except Exception as e:
            print(f"Error al buscar la película '{title}': {str(e)}")
    
    return jsonify({'movies': results}), 200