emp = {
    "e_id" :101,
    "name": "ABC",
    "age": 30,
    "department": "Field",
}

print("Before Deletion:")
print(emp)

del emp["department"]

print("After Deletion:")
print(emp)