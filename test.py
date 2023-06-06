import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('meteorite_data.csv', parse_dates=['year'], encoding='utf-8', low_memory=False)

# Convert 'year' column to datetime format
df['year'] = pd.to_datetime(df['year'], errors='coerce')

# Filter Earth meteorites that fell before the year 2000
earth_meteorites_before_2000 = df[(df['reclat'].notnull()) & (df['reclong'].notnull()) & (df['year'].dt.year < 2000)]

# Get the coordinates of Earth meteorites that fell before 1970
earth_meteorites_before_1970 = df[(df['reclat'].notnull()) & (df['reclong'].notnull()) & (df['year'].dt.year < 1970)]

# Get Earth meteorites with a mass greater than 10000 kg (10000 kg = 10000000 g)
earth_meteorites_mass_gt_10000kg = df[(df['reclat'].notnull()) & (df['reclong'].notnull()) & (df['mass'] > 10000)]

# Plotting the results
# Scatter plot of Earth meteorites before 2000
plt.figure(figsize=(10, 6))
plt.scatter(earth_meteorites_before_2000['reclong'], earth_meteorites_before_2000['reclat'], s=10)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Earth Meteorites Before 2000')
plt.grid(True)
plt.show()

# Scatter plot of Earth meteorites before 1970
plt.figure(figsize=(10, 6))
plt.scatter(earth_meteorites_before_1970['reclong'], earth_meteorites_before_1970['reclat'], s=10)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Earth Meteorites Before 1970')
plt.grid(True)
plt.show()

# Scatter plot of Earth meteorites with mass > 10000 kg
plt.figure(figsize=(10, 6))
plt.scatter(earth_meteorites_mass_gt_10000kg['reclong'], earth_meteorites_mass_gt_10000kg['reclat'], s=10)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Earth Meteorites with Mass > 10000 kg')
plt.grid(True)
plt.show()
