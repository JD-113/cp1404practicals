"""
Word Occurrences
Estimate: 30 minutes
Actual:   35  minutes
"""

word_to_count = {}
text = input("Enter a sentence: ")
words = text.split()
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

words = list(word_to_count.keys())
max_length = max(len(word) for word in words)

for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
