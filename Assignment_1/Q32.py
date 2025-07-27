students = {}
while True:
    print("\n1.Create 2.Read 3.Update 4.Delete 5.Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        roll = input("Enter roll number: ")
        name = input("Enter name: ")
        students[roll] = name
    elif choice == 2:
        print(students)
    elif choice == 3:
        roll = input("Enter roll to update: ")
        name = input("Enter new name: ")
        students[roll] = name
    elif choice == 4:
        roll = input("Enter roll to delete: ")
        students.pop(roll, None)
    elif choice == 5:
        break