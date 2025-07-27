import csv
with open("marks.csv", "r") as f:
    reader = csv.DictReader(f)
    subjects = {}
    count = 0
    for row in reader:
        count += 1
        for subject, mark in row.items():
            if subject != "Name":
                subjects[subject] = subjects.get(subject, 0) + float(mark)
    for subject in subjects:
        print(subject, "average =", subjects[subject]/count)