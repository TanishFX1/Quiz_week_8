import matplotlib.pyplot as plt
import pandas as pd

#Loading data from CSV file i nano-ed the file for this task and realised
# in my task 1 i wrote precipitation, so i've got Year, CO2 and Temperature.
data = pd.read_csv('climate.csv')

#Creating a figure for the plots (Not sure if width (15) and height (10) would be
#too big or small
plt.figure(figsize=(15, 10))

plt.subplot(1, 2, 1)
plt.plot(data['Year'], data['CO2'])
plt.title("CO2 Levels Over Time")
plt.xlabel("Year")
plt.ylabel("CO2 Levels")

plt.subplot(1, 2, 2)
plt.plot(data['Year'], data['Temperature'])
plt.title("Temperature Changes Over Time")
plt.xlabel("Year")
plt.ylabel("Temperature (C)")

# Display the plots
plt.tight_layout()
plt.show()
