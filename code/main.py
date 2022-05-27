from model.DSS import DSS, sum_prod, lukasiewicz, drastic_sum
import sqlite3
import pandas as pd
import database

efectividad = [12, 17, 25, 25]
altura = [170, 195, 220, 220]
sprint = [0, 0, 10, 15]


connection = sqlite3.connect('competitors.db')
cursor = connection.cursor()

print('Bienvenidx al sistema de asistencia de preselección de jugadores de Basketball')
print('¿Qué método de combinación de relglas desea usar?')
method = int(input('1: Máximo, 2: Suma-Producto, 3: Lukasiewicz, 4: Suma-Drástica: '))

if method == 2:
    method = sum_prod

elif method == 3:
    method = lukasiewicz

elif method == 4:
    method = drastic_sum

else:
    method = max

dss = DSS([efectividad, altura, sprint], [0.80, .95, 0.75], threshold=0.65, method=method)

while True:
    name = input('Ingrese el nombre del jugador/a: ')
    
    basket = int(input('Ingrese el número de canastas: '))
    while basket >25 or basket < 0 or type(basket) != int:
        basket = int(input('Ingrese un número de canastas válido (0 <= int <= 25): '))

    
    height = float(input('Ingrese su altura (cm): '))
    while height < 0:
        height = int(input('Ingrese una altura válida (0 <= float): '))

    time = float(input('Ingrese el tiempo de sprint (s): '))
    while time < 0:
        time = float(input('Ingrese un tiempo válido (0 <= int): '))

    score, text = dss(basket, height, time)
    print(f'El usuario {name} es adecuado para el equipo con certeza: {score}')
    print(text)

    cursor.execute('INSERT INTO competitors VALUES (?, ?, ?, ?, ?)', (name, basket, height, time, score))
    

    continue_ = input('\n¿Desea continuar? [y/n]: ')
    if continue_ == 'n':
        break

save = input('¿Desea guardar los datos?[y/n]: ')
if save == 'y':
    connection.commit()

data_frame = pd.read_sql_query("SELECT * FROM competitors ORDER BY score DESC" , connection)
connection.close()
print(data_frame)
