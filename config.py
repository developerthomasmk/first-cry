import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://DESKTOP-G1V72LF\SQLEXPRESS/firstcry_db?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False