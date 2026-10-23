
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Age': [23, 25, 28, 30, 32, 35, 37, 40, 42,
            45, 47, 50, 52, 55, 57, 60, 62, 65],
    'Fat': [15, 18, 20, 21, 22, 24, 25, 27, 28,
            30, 31, 33, 34, 35, 36, 38, 39, 40]
})

print("Mean:")
print(data.mean())

print("\nMedian:")
print(data.median())

print("\nStandard Deviation:")
print(data.std())

data.boxplot(column=['Age', 'Fat'])
plt.title("Boxplot")
plt.show()

plt.scatter(data['Age'], data['Fat'])
plt.xlabel("Age")
plt.ylabel("% Fat")
plt.title("Age vs Body Fat")
plt.show()

pd.plotting.qqplot(data['Age'], line='s')
plt.title("Q-Q Plot of Age")
plt.show()