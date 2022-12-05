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

    @classmethod
    def from_str(cls , string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0] , params[1] ,params[2])   #its the list 
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " +  string)

Jinal = Employee( "Jinal" , 50000 , "HR")
Robin = Employee("Robin" , 40000 , "Manager")  
Khushi = Employee.from_str("Khushi-30000-Instructor")

print(Robin.printdetails())
print(Jinal.printdetails())

print(Khushi.printgood("Khushi"))
# print(Jinal.salary)
# print(Robin.no_of_leaves)       
  