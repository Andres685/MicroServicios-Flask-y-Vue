from flask import Blueprint, request, jsonify
from .models import db, User, UserList
from .config import Config

routes = Blueprint('routes', __name__)

@routes.route('/mark_as_watched', methods=['POST'])
def mark_as_watched():

    data = request.get_json()
    user_id = data.get('user_id')
    movie_id = data.get('movie_id')

    if not user_id or not movie_id:
        return jsonify({'message': 'Faltan datos (se requieren user_id y movie_id)'}), 400

    user_movie = UserList.query.filter_by(user_id=user_id, movie_id=movie_id).first()

    if user_movie:
        if user_movie.watched:
            return jsonify({'message': 'La película ya está marcada como vista'}), 200
        else:
            user_movie.watched = True
    else:
        user_movie = UserList(user_id=user_id, movie_id=movie_id, watched=True)
        db.session.add(user_movie)
    
    db.session.commit()
    return jsonify({'message': 'Película marcada como vista'}), 200

@routes.route('/mark_as_not_watched', methods=['POST'])
def mark_as_not_watched():
    """
    Marca una película como no vista para un usuario específico.
    """
    data = request.get_json()
    user_id = data.get('user_id')
    movie_id = data.get('movie_id')

    if not user_id or not movie_id:
        return jsonify({'message': 'Faltan datos (se requieren user_id y movie_id)'}), 400

    user_movie = UserList.query.filter_by(user_id=user_id, movie_id=movie_id).first()

    if user_movie:
        if not user_movie.watched:
            return jsonify({'message': 'La película ya está marcada como no vista'}), 200
        else:
            user_movie.watched = False
    else:
        user_movie = UserList(user_id=user_id, movie_id=movie_id, watched=False)
        db.session.add(user_movie)
    
    db.session.commit()
    return jsonify({'message': 'Película marcada como no vista'}), 200

@routes.route('/watched', methods=['GET'])
def get_watched_movies():
    """
    Obtiene las películas que un usuario ha marcado como vistas.
    """
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'message': 'Se requiere user_id'}), 400
        
    watched_movies = UserList.query.filter_by(user_id=user_id, watched=True).all()
    movies = [entry.movie_id for entry in watched_movies]
    return jsonify({'watched_movies': movies}), 200

@routes.route('/not_watched', methods=['GET'])
def get_not_watched_movies():
    """
    Obtiene las películas que un usuario ha marcado como no vistas.
    """
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'message': 'Se requiere user_id'}), 400
        
    not_watched_movies = UserList.query.filter_by(user_id=user_id, watched=False).all()
    movies = [entry.movie_id for entry in not_watched_movies]
    return jsonify({'not_watched_movies': movies}), 200
