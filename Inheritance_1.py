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
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " +  string)




class Programmer(Employee):
    def __init__(self, aname, asalary, arole,alanguages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = alanguages
        
    def printprog(self):
        return f"The programmer's name is {self.name} , salary is {self.salary} , role is {self.role} , languages are {self.languages}"

Jinal = Employee( "Jinal" , 50000 , "HR")
Robin = Employee("Robin" , 40000 , "Manager")  
Khushi = Employee.from_str("Khushi-30000-Instructor")

print(Robin.printdetails())
print(Jinal.printdetails())

print(Khushi.printgood("Khushi"))

Krishna = Programmer("Krishna" , 20000 , "Programmer" , "J")
Harshit = Programmer("Harshit" , 25000 , "Programmer" ,["CPP" , "PYTHON"] )
print(Harshit.printprog())