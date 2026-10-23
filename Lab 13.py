from collections import Counter
import re

text = """Python is a programming language.
Python is easy to learn.
Data science uses Python.
Python is popular for data analysis."""

text = text.lower()

words = re.findall(r'\b\w+\b', text)

frequency = Counter(words)

print("Word Frequency:")

for word, count in frequency.items():
    print(word, ":", count)