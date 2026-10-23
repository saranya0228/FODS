import pandas as pd

sales_data = pd.DataFrame({
    'product': ['Laptop', 'Phone', 'Laptop', 'Mouse', 'Phone',
                'Keyboard', 'Laptop', 'Mouse'],
    'quantity': [5, 10, 3, 8, 7, 4, 6, 9]
})

top5 = sales_data.groupby('product')['quantity'].sum().sort_values(ascending=False).head(5)

print("Top 5 products sold:")
print(top5)