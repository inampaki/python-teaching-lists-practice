name = input("Entyer the name")
gender = input("Entyer the gender")
age = int(input("Enter the age"))
if(age < 20 and gender == 'Male'):
    print(name," Please sit in first 2 rwos ")
elif(age >= 20 and gender == 'Male'):
    print(name," Seat in the middle 3 rows")
else:
    print("Please sit in last rows!")