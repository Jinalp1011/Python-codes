def Fibonacci(n):
    a = 0
    b = 1

    if n < 0:
        print("Enter valid input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

number = int(input("Enter the number"))
print(Fibonacci(number))
