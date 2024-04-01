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

#Write your code below this line 👇
import random

rps = [rock, paper, scissors]
choice = int(input("What do you choose? Please type 0 for Rock, 1 for Paper, or 2 Scissors.\n"))
if choice >= 3 or choice < 0:
    print("You typed an invalid number, so you lose, butthead.")
else:
    print(rps[choice])

cpuchoice = random.randint(0,2)
print("Computer chose:")
print(rps[cpuchoice])
if choice == 0 and cpuchoice == 2:
    print("You won!")
elif cpuchoice == 0 and choice == 2:
    print("You lose!")
elif cpuchoice > choice:
    print("You lose!")
elif choice > cpuchoice:
    print("You win!")
elif choice == cpuchoice:
    print("Draw!")