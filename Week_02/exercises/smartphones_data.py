import pandas as pd
import numpy as np
import random

# Define the possible values for each variable
makes = ['Apple', 'Samsung', 'Google', 'OnePlus', 'Xiaomi']
models = ['Model A', 'Model B', 'Model C', 'Model D', 'Model E']
prices = np.random.uniform(300, 1200, 1000)
camera_resolutions = np.random.randint(8, 108, 1000)
battery_life_hours = np.random.randint(10, 48, 1000)
storage_sizes = np.random.choice([64, 128, 256, 512], 1000)
screen_sizes = np.random.uniform(5.0, 7.0, 1000)

# Create the data set
data = {
    'make': np.random.choice(makes, 1000),
    'model': np.random.choice(models, 1000),
    'price': prices,
    'camera_resolution': camera_resolutions,
    'battery_life_hours': battery_life_hours,
    'storage_size': storage_sizes,
    'screen_size': screen_sizes
}

# Convert to a DataFrame
df = pd.DataFrame(data)

# Write the data to an Excel file
df.to_excel('smartphones_data.xlsx', index=False)

print("Data set created and saved to 'smartphones_data.xlsx'")