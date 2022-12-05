#----CLASSES = TEMPLATE------
#------OBJECT = INSTANCE OF THE CLASS-----

# DRY ---> DO NOT REPEAT YOURSELF
class Student:
    pass      # when u dont have to write any thing 

Jinal = Student()
Khushi = Student()

Jinal.name = "Jinal"
Jinal.std = 12
Jinal.section = 1
Khushi.name = "Khushi"
Khushi.subject = ["Physics","Maths"]

print(Jinal.name , Khushi.subject)