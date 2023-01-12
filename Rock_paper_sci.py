import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock Paper Scissors Game\nHope you win against the computer!")
print("0 for Rock, 1 for Paper and 2 for Scissors")
choice = int(input("Choose : "))
comp = random.randint(0, 2)
game_images = [rock, paper, scissors]
if choice not in [0, 1, 2]:
    print("You already lost!! Wrong input")
    exit(1)
print("You chose : ")
print(game_images[choice])
print("Computer chose : ")
print(game_images[comp])

# rock 0 paper 1 and scissors 2
if choice == 0:
    if comp == 1:
        print("You lost :( ")
    elif comp == 2:
        print("Congrats!! You won :) ")
    else:
        print("Its a tie")
elif choice == 1:
    if comp == 0:
        print("Congrats!! You won :) ")
    elif comp == 1:
        print("Its a tie")
    else:
        print("You lost :( ")
else:
    if comp == 0:
        print("You lost :( ")
    elif comp == 1:
        print("Congrats!! You won :) ")
    else:
        print("Its a tie")
