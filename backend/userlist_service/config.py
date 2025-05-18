# config.py
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:admin@localhost/pelis'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OMDB_API_KEY = '52321182'  # Aquí va tu API key de OMDb
    OMDB_URL = "https://www.omdbapi.com/"
