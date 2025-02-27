"""
This module demonstrates creating a DataFrame using pandas.
"""

# Import libraries
import pandas as pd

# Initialize data of lists
data = {
    'Name': ['Tom', 'Nick', 'Krish', 'Jack'],
    'Age': [20, 21, 19, 18]
}

# Create DataFrame
df = pd.DataFrame(data)
print(type(df))

# Print the output
print(df.head())
