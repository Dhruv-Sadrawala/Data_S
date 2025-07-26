#Find topper from above program.

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

sorted_students = sorted(dict1.items(), key=lambda item: item[1][4], reverse=True)
highest_total = sorted_students[0][1][4]
top_scorers = [(s_id, details[0]) for s_id, details in sorted_students if details[4] == highest_total]

print("___________________________")
print("Topper Student")
for s_id, name in top_scorers:
    print(f"Name: {name}, Total Marks: {highest_total}")
print("___________________________")