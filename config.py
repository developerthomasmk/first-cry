import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://MSI\SQLEXPRESS/firstcry_db?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False