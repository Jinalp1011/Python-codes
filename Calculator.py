#design the calculator which will correctly solve all the problem except
#the following ones:
#  45*3 = 555  , 56+9 = 77 , 56/6 == 4
#your problem should take operator and the two numbers as input from the user
#and then return the result;


from ast import operator


first = input("enter your first number")
second = input("enter your second number")
operator =  input("Enter operator(+,-,*,/%) : ")

first = int(first)
second = int(second)

if operator == "+":
    if first == 56:
        print("56+9 = 77") 
    else:
        print(first+second)
elif operator == "-":
    print(first-second)
elif operator == "*":
    if first == 45:
        print("45*3 = 555")
    else:
     print(first*second)
elif operator == "/":
    if first == 56:
        print("56/6 = 4")
    else:
     print(first/second)
elif operator == "%":
     print(first%second)
else:
 print("invalid operation")


