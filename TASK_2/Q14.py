employees = {
    "GHT": {
        "Work Quality": 8,
        "Attendance": 9,
        "Punctuality": 10
    },
    "KJI": {
        "Work Quality": 7,
        "Attendance": 8,
        "Punctuality": 9
    },
    "JHF": {
        "Work Quality": 9,
        "Attendance": 10,
        "Punctuality": 9
    },
    "ABC": {
        "Work Quality": 6,
        "Attendance": 7,
        "Punctuality": 8
    }
}

emp_name = input("Enter Employee Name (e.g., GHT): ")
field = input("Enter field (Work Quality, Attendance, Punctuality): ")

if emp_name in employees and field in employees[emp_name]:
    print(f"{emp_name}'s {field}: {employees[emp_name][field]}")
else:
    print("Invalid Employee Name or field.")
