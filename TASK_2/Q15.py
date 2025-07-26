patients = {}

n = int(input("Enter the number of patient records: "))

for i in range(n):
    print(f"\nEnter details for patient {i + 1}:")
    p_id = int(input("Enter Patient ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    illness = input("Enter Illness: ")
    

    patients[p_id] = {
        "Name": name,
        "Age": age,
        "Illness": illness
    }

print("\nPatient Records:")
for pid, details in patients.items():
    print(f"ID: {pid}, Name: {details['Name']}, Age: {details['Age']}, Illness: {details['Illness']}")
