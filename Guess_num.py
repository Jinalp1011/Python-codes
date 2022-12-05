n = 18  #num
m = 1   #total num of guess

print("You have only 9 number of guess")
#number = input("please enter your number")

while (m <= 9):
    guess_num = int(input("Guess the number.\n")) 
    if guess_num < 18:
     print("You enter less number please kindly input greater number\n")
    elif guess_num > 18:
      print("You enter greater number please kindly input less number\n")
    else:
        print("you won\n")
        print(m , "no.of guess he took to finish the game")
        break
  
    print("left guess number",m)
    m = m+1

if(m >= 9):
        print("Game over\n you lose the game")
