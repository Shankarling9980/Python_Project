import string
from collections import Counter

text = input("Enter a paragraph:")

text = text.lower()

text = text.translate(str.maketrans('', '', string.punctuation))

words = text.split()
word_counts = Counter(words)


sorted_word_counts = sorted(word_counts.items())  # alphabetically
most_freq = max(word_counts.values())

print("Word Frequency:")
for word, count in sorted_word_counts:
    highlight = "*" if count == most_freq else ""
    print(f"{word}: {count}{highlight}")

print("Histogram:")
for word, count in sorted_word_counts:
    print(f"{word:12} {'#' * count}")

with open("word_frequency.txt", "w") as f:
    for word, count in sorted_word_counts:
        f.write(f"{word}: {count}")
        