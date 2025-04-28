from flask import Blueprint, jsonify, request
import requests
from config import Config

routes = Blueprint('routes', __name__)

TMDB_API_KEY = Config.TMDB_API_KEY
TMDB_URL = Config.TMDB_URL

# Endpoint para buscar películas por título
@routes.route('/movies', methods=['GET'])
def get_movies():
    title = request.args.get('title', '')
    
    if not title:
        return jsonify({"message": "Debe proporcionar un título de película"}), 400

    try:
        response = requests.get(
            f"{TMDB_URL}/search/movie",
            params={
                'api_key': TMDB_API_KEY,
                'query': title,
                'language': 'es-ES',
            }
        )

        if response.status_code == 200:
            data = response.json()
            if data['results']:
                return jsonify(data['results']), 200
            else:
                return jsonify({"message": "No se encontraron películas"}), 404
        else:
            return jsonify({
                "message": f"Error al consultar TMDB API: {response.status_code}",
                "details": response.text
            }), 500
    except Exception as e:
        return jsonify({"message": "Error interno en el servidor", "error": str(e)}), 500

# Endpoint para obtener películas con paginación
@routes.route('/movies/paginated', methods=['GET'])
def get_paginated_movies():
    page = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=20, type=int)

    try:
        response = requests.get(
            f"{TMDB_URL}/movie/popular",
            params={
                'api_key': TMDB_API_KEY,
                'language': 'es-ES',
                'page': page,
            }
        )

        if response.status_code == 200:
            data = response.json()
            total_results = data['total_results']
            movies = data['results']
            return jsonify({
                "movies": movies,
                "total_results": total_results,
                "total_pages": (total_results // limit) + 1,
                "current_page": page
            }), 200
        else:
            return jsonify({
                "message": f"Error al consultar TMDB API: {response.status_code}",
                "details": response.text
            }), 500
    except Exception as e:
        return jsonify({"message": "Error interno en el servidor", "error": str(e)}), 500