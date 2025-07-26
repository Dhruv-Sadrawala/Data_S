# Write a program to add a new patient record (ID, name, age, disease) to an existing dictionary
# and display the updated dictionary

patients = {}

patients[101] = "ABC",12,"TB"
patients[102] = "UIO",14,"GH"

print("Insert a new record in dictionary.")
p_id = int(input("Enter Patient ID: "))
p_name = input("Enter Patient Name: ")
p_age = int(input("Enter Patient Age: "))
p_disease = input("Enter Patient Disease: ")

patients[p_id] = p_name,p_age,p_disease

print(patients)