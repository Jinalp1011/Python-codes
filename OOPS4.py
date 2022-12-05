class Employee:
    no_of_leaves = 8
    def __init__(self , aname , asalary , arole):   #constructor 
        self.name = aname
        self.salary = asalary
        self.role = arole
        

    def printdetails(self):  
        return f"Name is {self.name} , salary is {self.salary} , role is {self.role}"
    
    @classmethod
    def change_leaves(cls , new_leaves):
       cls.no_of_leaves = new_leaves
        

Jinal = Employee( "Jinal" , 50000 , "HR")
Robin = Employee("Robin" , 40000 , "Manager")  

print(Robin.printdetails())
print(Jinal.printdetails())
print(Jinal.salary)
print(Robin.no_of_leaves)   # before you changed it
Employee.no_of_leaves = 9     # no of leaves changed for whole object
print(Robin.no_of_leaves)    #after you changed it 