emp_1 = {
    "e_id": 101,
    "name": "ABC",
    "age": 30,
    "department": "Field",
}
emp_2 = {
    "e_id": 102,
    "name": "FGT",
    "age": 34,
    "department": "Manager",
}

merged = emp_1 | emp_2

print(merged)