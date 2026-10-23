import pandas as pd

data = pd.DataFrame({
    'age': [20, 25, 20, 30, 25, 30, 20, 35, 25, 30]
})

frequency = data['age'].value_counts().sort_index()

print("Age Frequency Distribution:")
print(frequency)