patients = [["Aman", 21], ["Riya", 24], ["Karan", 30]]

new_name = input("Enter patient name to add: ")
new_age = int(input("Enter patient age: "))
patients.append([new_name, new_age])

search_name = input("Enter patient name to search: ")
found = False
for patient in patients:
    if patient[0] == search_name:
        print("Patient found:", patient[0], patient[1])
        found = True
        break
if not found:
    print("Patient not found")

delete_name = input("Enter patient name to delete: ")
removed = False
for patient in patients:
    if patient[0] == delete_name:
        patients.remove(patient)
        removed = True
        print("Patient deleted")
        break
if not removed:
    print("Patient not found")

print("All patients:")
for patient in patients:
    print("Name:", patient[0], "Age:", patient[1])

print("Total patients:", len(patients))
