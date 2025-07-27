with open("students.txt", "r") as src, open("copy.txt", "w") as dest:
    for line in src:
        dest.write(line)