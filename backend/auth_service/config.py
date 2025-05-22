import os

class Config:
    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc://Adminbd:Admin123*@serversqlazureag.database.windows.net:1433/"
        "PeliculasFlask?driver=ODBC+Driver+17+for+SQL+Server&Encrypt=yes"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "123")
