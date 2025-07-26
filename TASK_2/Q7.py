patients = [{
    "p_id":101,
    "name" : "FGT",
    "disease": "Flu"
},
{
    "p_id":102,
    "name" : "ABC",
    "disease": "Cold"
},
{
    "p_id":103,
    "name" : "XYZ",
    "disease": "Fever"
}]


for patient in patients:
    print(f"Patient ID: {patient['p_id']}, Name: {patient['name']}, Disease: {patient['disease']}")

p_id_c = int(input("Enter Patient ID to change disease: "))
for patient in patients:
    if patient['p_id'] == p_id_c:
        new_disease = input("Enter new disease: ")
        patient['disease'] = new_disease
        print(f"Updated Patient Record: {patient}")
        break
    else:
        print("Patient ID not found.")