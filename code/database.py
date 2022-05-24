from distutils.util import execute
import sqlite3

connection = sqlite3.connect('competitors.db')
cursor = connection.cursor()

try:
    cursor.execute("CREATE TABLE competitors (name text, baskets integer, height, time real, score real)")
except Exception as e:
    print(e)

connection.commit()
connection.close()
