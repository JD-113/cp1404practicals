"""
Word Occurrences
Estimate: 30 minutes
Actual:   35  minutes
"""

WORD_TO_COUNT = {}
text = input("Enter a sentence: ")
words = text.split()
for word in words:
    try:
        WORD_TO_COUNT[word] += 1
    except KeyError:
        WORD_TO_COUNT[word] = 1

words = list(WORD_TO_COUNT.keys())
max_length = max(len(word) for word in words)

for word in words:
    print(f"{word:{max_length}} : {WORD_TO_COUNT[word]}")
