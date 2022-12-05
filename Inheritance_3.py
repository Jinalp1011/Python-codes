class Dad:
    basketball = 1

class Son(Dad):
   dance = 1
   def isdance(self):
    return f"yes I dance {self.dance} no of times"

class GrandSon(Son):
    dance = 6

Harshit = Dad()
Robin = Son()
Parth = GrandSon()

print(Robin.isdance())
