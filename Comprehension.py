# ls = []
# for i in range(100):
#     if i%3 == 0:
#         ls.append(i)

# ls = [i for i in range(100) if i%3 == 0]
# print(ls)

# dict1 = {
#     i : f"item{i}" for i in range(1 , 1000) if i%100 == 0
# }
# dict2 ={value : key for key , value in dict1.items()}
# print(dict1 ,"\n \n" , dict2)

# dresses = {dress for dress in ["dress1" , "dress2" , "dress1" , "dress2"]}   #here use curly{} thats why its take variable only one time its called set compreh.
# print(dresses)

evens = (i for i in range(100) if i%2 ==0)
for even in evens:
    print(evens.__next__())