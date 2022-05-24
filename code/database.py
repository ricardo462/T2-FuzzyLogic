from distutils.util import execute
import sqlite3

connection = sqlite3.connect('competitors.db')
cursor = connection.cursor()

try:
    cursor.execute("CREATE TABLE competitors (name text, baskets integer, height, time real, score real)")
except:
    print('No se pudo crear la base de datos')

connection.commit()
connection.close()
