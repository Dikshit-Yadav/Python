sentence = input("Enter a sentence: ")

words = sentence.split()
freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

print("Word Frequency:")
for word, count in sorted_freq:
    print(word, ":", count)
