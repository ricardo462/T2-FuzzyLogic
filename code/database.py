from distutils.util import execute
import sqlite3

connection = sqlite3.connect('competitors.db')
try:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE competitors (name text, basckets integer, height, time real)")
except:
    print('No se pudo crear la base de datos')


personas = [('ric', 15, 183, 10), ('seb', 20, 182, 10)]
cursor.executemany('INSERT INTO competitors values (?, ?, ?, ?)', personas)


for row in cursor.execute('SELECT * FROM competitors'):
    print(row)

connection.close()
