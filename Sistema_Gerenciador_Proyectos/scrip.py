import sqlite3

# define connection and cursor

connection = sqlite3.connect('db.sqlite3')

cursor = connection.cursor()

# get results
consulta="*"
cursor.execute("SELECT "+ consulta +" FROM proyecto_proyecto")

results = cursor.fetchall()
print(results[1])
cursor.close()
connection.close()