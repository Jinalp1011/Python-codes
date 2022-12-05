# #ITERATIVE method

# def factorial(n):
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac
#     """
#      :param n : Integer
#      :return: n! = n * n-1 * n-2 * n-3.....1
#      n! = n * (n-1)!
#     """
    

# number = int(input("Enter the number"))
# print(factorial(number))

#RECURSIVE METHOD 

def factorial(n):
    if n ==1:
        return 1
    else:
        return n * factorial(n-1)
        
number = int(input("Enter the number"))
print(factorial(number))