import pandas as pd
from collections import Counter
import re

reviews = pd.DataFrame({
    'review': [
        'Good product and good quality',
        'Excellent product',
        'Good quality and excellent service'
    ]
})

text = ' '.join(reviews['review']).lower()

words = re.findall(r'\b\w+\b', text)

frequency = Counter(words)

print("Word Frequency:")

for word, count in frequency.items():
    print(word, ":", count)