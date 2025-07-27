word = input("Enter word to search: ")
with open("students.txt", "r") as f:
    for line in f:
        if word in line:
            print(line.strip())