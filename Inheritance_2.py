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


class Player:
    no_of_games = 4
    def __init__(self, name , game):
        self.name = name 
        self.game = game
    
    def printdetails(self):
        return f"Name is {self.name} , game is {self.game}"


class CoolProg(Employee , Player):  #order is imp
        languages = "cpp"
        def printlang(self):
            print(self.languages)

Jinal = Employee( "Jinal" , 50000 , "HR")
Robin = Employee("Robin" , 40000 , "Manager")  
Khushi = Employee.from_str("Khushi-30000-Instructor")

print(Robin.printdetails())
print(Jinal.printdetails())

print(Khushi.printgood("Khushi"))

Parth = Player("Parth" , {"Cricket"})
Harshit = CoolProg("Harshit" ,35000 , "CoolProgrammer" )
print(Harshit.printdetails())

