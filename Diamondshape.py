class A:
    def met(self):
        print("This is a method of class A\n")

class B(A):
    def met(self):
        print("This is a method of class B\n")

class C(A):
     def met(self):
        print("This is a method of class C\n")

class D(B,C):
     def met(self):
        print("This is a method of class D\n")

a = A()
b = B()
c = C()
d = D()
print(d.met())