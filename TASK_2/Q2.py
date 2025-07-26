# Program to store and display multiple employee records using a nested dictionary

emp = {}

size = int(input("Enter number of employees: "))

for i in range(size):
    id_e = int(input("\nEnter Employee ID: "))
    name = input("Enter Employee Name: ")
    sal = int(input("Enter Employee Salary: "))
    depart = input("Enter Employee Department: ")

   
    emp[id_e] = {
        "e_details": {
            "e_name": name,
            "e_sal": sal,
            "e_depart": depart
        }
    }

print("\nEmployee Records:")
for e_id, data in emp.items():
    details = data["e_details"]
    print(f"E_ID: {e_id}")
    print(f" Name: {details['e_name']}")
    print(f" Salary: {details['e_sal']}")
    print(f" Department: {details['e_depart']}")

