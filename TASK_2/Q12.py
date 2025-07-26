report = "The patient has flu . The flu is contagious and the patient needs rest."

words = report.split()

word_freq = {}

for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

print("Word Frequency in the Medical Report:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
