status=input("Enter Year (married/unmarried):")


if status=="married":
    print("company insures!!")

elif status=="unmarried":
    age=int(input("Enter age :"))
    gender=input("Enter gender (M/F):")
    if gender=="M" and age>=30:
        print("Company insures!!")
    if gender=="F" and age>=25:
        print("Company insures!!")
else:
    print("Company Doesnt insure.")


