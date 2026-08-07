students = ["Aman", "Riya", "Karan"]

print("Total students:", len(students))

search_name = input("Enter student name to search: ")
if search_name in students:
    print("Student is present")
else:
    print("Student is absent")

new_student = input("Enter new student name: ")
students.append(new_student)

absent_student = input("Enter absent student name to remove: ")
if absent_student in students:
    students.remove(absent_student)

print("Updated students:", students)
