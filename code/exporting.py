#### Exports the database information into a excel ####

if __name__ == "__main__":
    import sqlite3
    import pandas as pd

    connection = sqlite3.connect('competitors.db')
    data_frame = pd.read_sql_query("SELECT * FROM competitors ORDER BY score DESC" , connection)
    data_frame.to_excel('competitors.xlsx')

    connection.close()