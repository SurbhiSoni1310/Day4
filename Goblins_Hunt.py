import random
#Goblins hunt random game
print("Welcome to Goblins finding hunt !!")
choose = input("Choose the location of goblins hunt [1,10] : ")
any_num = random.randint(1, 10)
if choose == any_num:
    print("You won")
else:
    print("You lost, the goblins hunt was "+str(any_num))