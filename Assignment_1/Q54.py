import csv
data = [["Name", "Marks"], ["John", 90], ["Alice", 85]]
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)