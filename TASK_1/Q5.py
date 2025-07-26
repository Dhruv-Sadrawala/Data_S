# Write a Python program using a nested dictionary to store student records.

dict1 = {}
size = int(input("Enter number of students: "))
for i in range(size):
    s_id = input("Enter Student ID: ")
    s_name = input("Enter Name of student: ")
    s_maths = int(input("Enter Marks of Maths: "))
    s_science = int(input("Enter Marks of Science: "))
    s_english = int(input("Enter Marks of English: "))

    total = s_maths + s_science + s_english

    dict1[s_id] = {
        "name": s_name,
        "marks": {
            "Maths": s_maths,
            "Science": s_science,
            "English": s_english,
            "Total": total
        }
    }

print("Student Records:")
for s_id, details in dict1.items():
    print(f"{s_id} => Name: {details['name']}, Total Marks: {details['marks']['Total']}")

# print(dict1)