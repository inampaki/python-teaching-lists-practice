a = "Waqas"
print(type(a))
first_num = int(input("Enter first num"))
sec_num = int(input("Enter 2nd Num"))
operator = input("Please enter following operator (+,-,/,*")

if operator == "/":
    print(first_num/sec_num)
elif operator == '+':
    print(first_num + sec_num)
else:
    print('Invalid Operator')
print('Bye Bye')