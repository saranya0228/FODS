import pandas as pd

order_data = pd.DataFrame({
    'customer_id': [101, 102, 101, 103, 102, 101],
    'order_date': ['2026-01-10', '2026-01-12', '2026-01-15',
                   '2026-01-18', '2026-01-20', '2026-01-22'],
    'product_name': ['Laptop', 'Phone', 'Mouse', 'Laptop', 'Phone', 'Keyboard'],
    'order_quantity': [1, 2, 3, 1, 1, 2]
})

order_data['order_date'] = pd.to_datetime(order_data['order_date'])

print("Total orders by each customer:")
print(order_data.groupby('customer_id').size())

print("\nAverage order quantity for each product:")
print(order_data.groupby('product_name')['order_quantity'].mean())

print("\nEarliest order date:", order_data['order_date'].min())
print("Latest order date:", order_data['order_date'].max())