import pandas as pd

property_data = pd.DataFrame({
    'property_id': [1, 2, 3, 4, 5],
    'location': ['Chennai', 'Bangalore', 'Chennai', 'Mumbai', 'Bangalore'],
    'bedrooms': [3, 5, 4, 6, 2],
    'area': [1200, 2500, 1800, 3000, 1000],
    'price': [5000000, 9000000, 6500000, 12000000, 4000000]
})

print("Average listing price by location:")
print(property_data.groupby('location')['price'].mean())

print("\nProperties with more than 4 bedrooms:")
print((property_data['bedrooms'] > 4).sum())

print("\nProperty with largest area:")
print(property_data.loc[property_data['area'].idxmax()])