import sqlite3
import pandas as pd
from model.DSS import DSS, sum_prod, lukasiewicz, drastic_sum

#### Creates the scores for the other methods ####
connection = sqlite3.connect('competitors.db')
cursor = connection.cursor()
writer = connection.cursor() 

efectividad = [12, 17, 25, 25]
altura = [170, 195, 220, 220]
sprint = [0, 0, 10, 15]

dss_sum = DSS([efectividad, altura, sprint], [0.80, .95, 0.75], threshold=0.65, method=sum_prod)
dss_luka = DSS([efectividad, altura, sprint], [0.80, .95, 0.75], threshold=0.65, method= lukasiewicz)
dss_drastic = DSS([efectividad, altura, sprint], [0.80, .95, 0.75], threshold=0.65, method=drastic_sum)

try:
    cursor.execute('CREATE TABLE comparing_methods (name text, max real, sum_prod real, lukasiewicz real, drastic_sum real)')
except Exception as e:
    print('comparing_methods generation: \n')
    print(e)

data = cursor.execute('SELECT * FROM competitors')

for row in data:
    name, basket, height, time, score = row[0], row[1], row[2], row[3], row[4]
    
    score_sum, text = dss_sum(basket, height, time)
    score_luka, text = dss_luka(basket, height, time)
    score_drastic, text = dss_drastic(basket, height, time)

    writer.execute('INSERT INTO comparing_methods VALUES (?, ?, ?, ?, ?)', (name, score, score_sum, score_luka, score_drastic))


data_frame = pd.read_sql_query("SELECT * FROM comparing_methods ORDER BY max DESC" , connection)


with pd.ExcelWriter('competitors.xlsx',engine='openpyxl', mode='a') as writer: 
    data_frame.to_excel(writer, sheet_name='comparing_methods')

connection.commit()   


connection.close()

print(data_frame)