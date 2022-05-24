from model.DSS import DSS
import sqlite3
import pandas as pd
import database

efectividad = [12, 17, 25, 25]
altura = [170, 195, 220, 220]
sprint = [0, 0, 10, 15]

dss = DSS([efectividad, altura, sprint], [0.80, .95, 0.75], threshold=0.9)
connection = sqlite3.connect('competitors.db')
cursor = connection.cursor()

print('Bienvenidx al sistema de asistencia de preselección de jugadores de Basketball')

while True:
    name = input('Ingrese el nombre del jugador/a:')
    
    basket = int(input('Ingrese el número de canastas'))
    while basket >25 or basket < 0 or type(basket) != int:
        basket = int(input('Ingrese un número de canastas válido (0 <= int <= 25)'))

    
    height = float(input('Ingrese su altura (cm)'))
    while height < 0:
        height = int(input('Ingrese una altura válida (0 <= float)'))

    time = float(input('Ingrese el tiempo de sprint (s)'))
    while time < 0:
        time = float(input('Ingrese un tiempo válido (0 <= int)'))

    score, text = dss(basket, height, time)
    print(f'El usuario {name} es adecuado para el equipo con certeza: {score}')

    cursor.execute('INSERT INTO competitors VALUES (?, ?, ?, ?, ?)', (name, basket, height, time, score))
    connection.commit()

    continue_ = input('¿Desea continuar? [y/n]')
    if continue_ == 'n':
        break

data_frame = pd.read_sql_query("SELECT * FROM competitors" , connection)
connection.close()
print(data_frame)