students = {}
roll = input("Enter roll number: ")
name = input("Enter name: ")
marks = float(input("Enter marks: "))
students[roll] = {"name": name, "marks": marks}
print(students)