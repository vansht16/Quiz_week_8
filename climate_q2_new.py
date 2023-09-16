
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the climate.csv file
climate_data = pd.read_csv('climate.csv')

# Extracting data into the provided lists
years = climate_data['Year'].tolist()
co2 = climate_data['CO2'].tolist()
temp = climate_data['Temperature'].tolist()

# Plotting using the provided graph structure
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 

plt.tight_layout()
plt.show() 
plt.savefig("co2_temp_2.png")
