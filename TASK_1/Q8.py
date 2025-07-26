# Each patient has a unique Patient ID, a name, and a dictionary of test results for three health
# parameters: Blood Pressure, Blood Sugar, and Cholesterol Level.


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

print(dict1)