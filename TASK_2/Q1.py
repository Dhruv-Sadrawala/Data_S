# Create a program that performs CRUD operations on a patient dictionary, where patient IDs are
# the keys and names are the values.

patient = {}

#c
patient[101] = "ABC"
patient[102] = "UIO"

print("----------------------")
print("Normal Dictionary")
print(patient)
print("----------------------")


#r
print("----------------------")
print("Reading Dictionary")
for pid,name in patient.items():
	print(f"P_ID:{pid},Patient Name: {name}")
print("----------------------")

#u
patient[101] = "THY"

print("----------------------")
print("Updated Dictionary")
print(patient)
print("----------------------")

#d
del patient[ ]

print("----------------------")
print("Deleted Record 102 from Dictionary")
print(patient)
print("----------------------")