import sqlite3

# Connect to the climate.db database
database_connection = sqlite3.connect('climate.db')
#A "cursor" is used to retrieve data from the database
cursor = database_connection.cursor()

#Create empty lists that will be populated!
years = []
temperatures = []
precipitations = []

try:
    cursor.execute('SELECT year, temperature, precipitation FROM climate_data')
    rows = cursor.fetchall()
    for row in rows:
        years.append(row[0])
        temperatures.append(row[1])
        precipitations.append(row[2])
finally:
    #Good practice to close the database after done with it
    database_connection.close()

print("First 10 years:", years)
print("First 10 temperatures:", temperatures)
print("First 10 precipitations:", precipitations)
