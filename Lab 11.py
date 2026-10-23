import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [100, 150, 130, 180, 200, 220]

plt.plot(months, sales, marker='o')
plt.title('Monthly Sales - Line Plot')
plt.show()

plt.scatter(months, sales)
plt.title('Monthly Sales - Scatter Plot')
plt.show()

plt.bar(months, sales)
plt.title('Monthly Sales - Bar Plot')
plt.show()