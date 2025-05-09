from flask import Blueprint, jsonify, request
import requests
from flask_cors import cross_origin
from .config import Config

routes = Blueprint('routes', __name__)

# Endpoint para buscar películas
@routes.route('/api/movies/search', methods=['GET'])
def search_movies():
    query = request.args.get('query', '')
    page = request.args.get('page', default=1, type=int)
    
    if not query:
        return jsonify({"error": "El parámetro 'query' es obligatorio"}), 400

    try:
        response = requests.get(
            f"{Config.TMDB_URL}/search/movie",
            params={
                'api_key': Config.TMDB_API_KEY,
                'query': query,
                'language': 'es-ES',
                'page': page,
                'include_adult': False
            }
        )
        response.raise_for_status()
        data = response.json()
        return jsonify(data), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para películas populares
@routes.route('/api/movies/popular', methods=['GET'])
def popular_movies():
    page = request.args.get('page', default=1, type=int)
    
    try:
        response = requests.get(
            f"{Config.TMDB_URL}/movie/popular",
            params={
                'api_key': Config.TMDB_API_KEY,
                'language': 'es-ES',
                'page': page
            }
        )
        response.raise_for_status()
        data = response.json()
        return jsonify(data), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para detalles de película
@routes.route('/api/movies/<int:movie_id>', methods=['GET'])
def movie_details(movie_id):
    try:
        response = requests.get(
            f"{Config.TMDB_URL}/movie/{movie_id}",
            params={
                'api_key': Config.TMDB_API_KEY,
                'language': 'es-ES',
                'append_to_response': 'credits,videos'
            }
        )
        response.raise_for_status()
        data = response.json()
        return jsonify(data), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para listar géneros
@routes.route('/api/genres', methods=['GET'])
def list_genres():
    try:
        response = requests.get(
            f"{Config.TMDB_URL}/genre/movie/list",
            params={
                'api_key': Config.TMDB_API_KEY,
                'language': 'es-ES'
            }
        )
        response.raise_for_status()
        data = response.json()
        return jsonify(data), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para películas por género
@routes.route('/api/movies/genre/<int:genre_id>', methods=['GET'])
def movies_by_genre(genre_id):
    page = request.args.get('page', default=1, type=int)
    
    try:
        response = requests.get(
            f"{Config.TMDB_URL}/discover/movie",
            params={
                'api_key': Config.TMDB_API_KEY,
                'language': 'es-ES',
                'with_genres': genre_id,
                'page': page,
                'sort_by': 'popularity.desc'
            }
        )
        response.raise_for_status()
        data = response.json()
        return jsonify(data), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500