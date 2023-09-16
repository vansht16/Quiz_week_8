
import sqlite3
import matplotlib.pyplot as plt

def fetch_data_from_db(db_path):
    # Establishing a connection to the database
    connection = sqlite3.connect(db_path)
    cur = connection.cursor()

    # Query to extract all records from ClimateData table
    query = "SELECT Year, CO2, Temperature FROM ClimateData"
    cur.execute(query)
    
    # Fetching the results and closing the connection
    records = cur.fetchall()
    connection.close()

    # Separating the data into individual lists
    years_data, co2_data, temperature_data = [], [], []
    for record in records:
        years_data.append(record[0])
        co2_data.append(record[1])
        temperature_data.append(record[2])

    return years_data, co2_data, temperature_data

# Fetching the data from the database
years, co2, temp = fetch_data_from_db('climate.db')

# Plotting using the provided graph structure
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data from Database") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 

plt.tight_layout()
plt.show() 
plt.savefig("co2_temp_1.png")
