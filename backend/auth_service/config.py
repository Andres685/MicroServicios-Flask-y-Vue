class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:admin@localhost/pelis'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = '123'