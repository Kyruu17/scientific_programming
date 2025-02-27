import pandas as pd

# Load the data
data = pd.read_csv('/workspaces/scientific_programming/Week_02/exercises/data/BigmacPrice.csv')

# Filter data for Switzerland and the U.S.A. for the years 2002 and 2022
switzerland_2002 = data[(data['name'] == 'Switzerland') & (data['date'].str.startswith('2002'))]['dollar_price'].values[0]
switzerland_2022 = data[(data['name'] == 'Switzerland') & (data['date'].str.startswith('2022'))]['dollar_price'].values[0]
usa_2002 = data[(data['name'] == 'United States') & (data['date'].str.startswith('2002'))]['dollar_price'].values[0]
usa_2022 = data[(data['name'] == 'United States') & (data['date'].str.startswith('2022'))]['dollar_price'].values[0]

# Calculate the price changes
switzerland_change = switzerland_2022 - switzerland_2002
usa_change = usa_2022 - usa_2002

# Print the results
print(f"Big Mac price change in Switzerland (2002-2022): {switzerland_change}")
print(f"Big Mac price change in the U.S.A. (2002-2022): {usa_change}")

# Compare the price changes
if switzerland_change > usa_change:
    print("The Big Mac price increase in Switzerland is higher compared to the U.S.A.")
else:
    print("The Big Mac price increase in the U.S.A. is higher compared to Switzerland.")