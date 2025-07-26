
emp = {}
emp[101] = 'ABC', 30 ,'Field',23000
emp[102] = 'FGT', 34 ,'Manager',24000
emp[103] = 'UII', 37 ,'Clerk',25000

for key, value in emp.items():
    print(f"Name: {value[0]}, Salary: {value[3]}")