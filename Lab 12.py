import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
temperature = [25, 27, 29, 32, 34, 33]
rainfall = [20, 30, 40, 60, 80, 100]

plt.plot(months, temperature, marker='o')
plt.xlabel('Month')
plt.ylabel('Temperature')
plt.title('Monthly Temperature')
plt.show()

plt.scatter(months, rainfall)
plt.xlabel('Month')
plt.ylabel('Rainfall')
plt.title('Monthly Rainfall')
plt.show()