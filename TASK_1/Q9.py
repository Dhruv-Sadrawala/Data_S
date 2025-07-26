
dict1 = {}
size = int(input("Enter number of patients: "))
for i in range(size):
    p_id = input("Enter Patient ID: ")
    p_name = input("Enter Name of patient: ")
    p_bp = int(input("Enter Blood Pressure: "))
    p_bs = int(input("Enter Blood Sugar: "))
    p_cl = int(input("Enter Cholesterol Level: "))
    
    total = p_bp + p_bs + p_cl
    
    dict1[p_id] = {
        "name": p_name,
        "details": {
            "Blood Pressure": p_bp,
            "Blood Sugar": p_bs,
            "Cholesterol Level": p_cl,
            "Total Health Score": total
        }
    }

print("___________________________")
print("Patients Name and Total Health Scores")
for p_id, details in dict1.items():
    print(f"Name: {details['name']}, Total Health Score: {details['details']['Total Health Score']}")
print("___________________________")

healthiest_patient = min(dict1.items(), key=lambda item: item[1]['details']['Total Health Score'])

print("___________________________")
print("Patient with Lowest Health Score (Healthiest)")
print(f"Name: {healthiest_patient[1]['name']}, Total Health Score: {healthiest_patient[1]['details']['Total Health Score']}")
print("___________________________")
