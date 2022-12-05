class Employee:
    no_of_leaves = 8
    def __init__(self , aname , asalary , arole):   #constructor 
        self.name = aname
        self.salary = asalary
        self.role = arole
        

    def printdetails(self):  
        return f"Name is {self.name} , salary is {self.salary} , role is {self.role}"
    

Jinal = Employee( "Jinal" , 50000 , "HR")
Robin = Employee("Robin" , 40000 , "Manager")   

# Jinal.name = "Jinal"
# Jinal.salary = 50000
# Jinal.role = "HR"

# Robin.name = "Robin"
# Robin.salary = 40000
# Robin.role = "Manager"

print(Robin.printdetails())
print(Jinal.printdetails())
print(Jinal.salary)