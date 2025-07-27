freq = {}
with open("students.txt", "r") as f:
    for line in f:
        for word in line.split():
            freq[word] = freq.get(word, 0) + 1
print(freq)