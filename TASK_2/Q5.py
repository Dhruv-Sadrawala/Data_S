# Write a program to check if a patient record contains the key “age” using the in operator and print
# the age if present.

patient_record = {
    "name": "John Doe",
    "age": 30,
    "disease": "Flu",
}

if "age" in patient_record:
    print(f"Age: {patient_record['age']}")
else:
    print("Age not found in patient record.")