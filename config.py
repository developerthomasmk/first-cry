import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://91807@MSI\91807/firstcry_db?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False