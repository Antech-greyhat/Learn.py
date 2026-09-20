from collections import Counter
sentence = 'the quick brown fox jumps over the lazy dog the fox runs'
words = sentence.split()
print(words)

unique_words = set(words)
print(unique_words)
print(f'There are {len(unique_words)} unique words out of {len(words)} total words')

word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print(word_counts)

for word, count in word_counts.items():
    print(f'"{word} appeared: {count} times(s)')

print(Counter(words).most_common(1))