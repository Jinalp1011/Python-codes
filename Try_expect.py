f1 = open("File.txt")

try:
    f = open("Does.txt")

except Exception as e:
    print(e)

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway")
    f1.close()

print("Imp stuff")