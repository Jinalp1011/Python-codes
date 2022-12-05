class Employee:
    no_of_leaves = 8
    pass

Jinal = Employee()
Robin = Employee()   

Jinal.name = "Jinal"
Jinal.salary = 50000
Jinal.role = "HR"

Robin.name = "Robin"
Robin.salary = 40000
Robin.role = "Manager"

print(Jinal.salary)

print(Robin.no_of_leaves)
Employee.no_of_leaves = 9
print(Jinal.no_of_leaves)
print(Jinal.__dict__)
print(Robin.__dict__)