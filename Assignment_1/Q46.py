students = {}
n = int(input("How many students? "))
for _ in range(n):
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks
print(students)