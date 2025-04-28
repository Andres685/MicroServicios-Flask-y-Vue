# config.py
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:admin@localhost/pelis'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TMDB_API_KEY = '6223f8fd378aa549ccaf7d7199446c39'
    TMDB_URL = "https://api.themoviedb.org/3"