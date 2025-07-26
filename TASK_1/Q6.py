# 6. Each student has a unique student ID, a name, and a dictionary of marks for three
# subjects: Math, Science, and English.
# Perform the following tasks:
# 1. Store the details of at least three students using a nested dictionary format.
# 2. Iterate through the dictionary and print each student’s name and their total marks.


dict1 = {}
size = int(input("Enter number of students: "))
for i in range(size):
    s_id = input("Enter Student ID: ")
    s_name = input("Enter Name of student: ")
    s_maths = int(input("Enter Marks of Maths: "))
    s_science = int(input("Enter Marks of Science: "))
    s_english = int(input("Enter Marks of English: "))
    
    total = s_maths+s_science+s_english
    
    dict1[s_id] = s_name,s_maths,s_science,s_english,total

print("___________________________")
print("Students Name and Marks")
for s_id, details in dict1.items():
    s_name, _, _, _, total = details
    print(f"Name: {s_name}, Total Marks: {total}")
print("___________________________")