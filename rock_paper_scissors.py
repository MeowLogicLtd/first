#Title
print("===================")
print("Rock Paper Scissors")
print("===================")
print("1) ✊")
print("2) ✋")
print("3) ✌️")

#Asking player and CPU to play
player = int(input("Pick a number (1-3): "))
import random
computer = random.randint(1, 3)

#Announcing who chose what
if player == 1:
  print("You chose: ✊")
elif player == 2:
  print("You chose: ✋")
elif player == 3:
  print("You chose: ✌️")
else:
  print("Choose a valid option.")

if computer == 1:
  print("CPU chose: ✊")
elif computer == 2:
  print("CPU chose: ✋")
elif computer == 3:
  print("CPU chose: ✌️")
else:
  print("CPU made an error.")

#Calculating the winner
if player == computer:
  print("It's a tie!") 
elif player == 1 and computer == 2:
  print("The CPU won!")
elif player == 1 and computer == 3:
  print("The player won!")
elif player == 2 and computer == 1:
  print("The player won!")
elif player == 2 and computer == 3:
  print("The CPU won!")
elif player == 3 and computer == 1:
  print("The CPU won!")
elif player == 3 and computer == 2:
  print("The player won!")
else:
  print("Error.")


#Title
print("================================")
print("Rock Paper Scissors Lizard Spock")
print("================================")
print("1) ✊")
print("2) ✋")
print("3) ✌️")
print("4) 🦎")
print("5) 🖖")

#Asking player and CPU to play
player = int(input("Pick a number (1-5): "))
import random
computer = random.randint(1, 5)

#Announcing who chose what
if player == 1:
  print("You chose: ✊")
elif player == 2:
  print("You chose: ✋")
elif player == 3:
  print("You chose: ✌️")
elif player == 4:
  print("You chose: 🦎")
elif player == 5:
  print("You chose: 🖖")
else:
  print("Choose a valid option.")

if computer == 1:
  print("CPU chose: ✊")
elif computer == 2:
  print("CPU chose: ✋")
elif computer == 3:
  print("CPU chose: ✌️")
elif computer == 4:
  print("CPU chose: 🦎")
elif computer == 5:
  print("CPU chose: 🖖")
else:
  print("CPU made an error.")


if player == computer:
  print("It's a tie!") 
elif player == 1 and computer == 2:
  print("The CPU won!")
elif player == 1 and computer == 3:
  print("The player won!")
elif player == 1 and computer == 4:
  print("The player won!")
elif player == 1 and computer == 5:
  print("The CPU won!")
elif player == 2 and computer == 1:
  print("The player won!")
elif player == 2 and computer == 3:
  print("The CPU won!")
elif player == 2 and computer == 4:
  print("The CPU won!")
elif player == 2 and computer == 5:
  print("The player won!")
elif player == 3 and computer == 1:
  print("The CPU won!")
elif player == 3 and computer == 2:
  print("The player won!")
elif player == 3 and computer == 4:
  print("The player won!")
elif player == 3 and computer == 5:
  print("The CPU won!")
elif player == 4 and computer == 1:
  print("The CPU won!")
elif player == 4 and computer == 2:
  print("The player won!")
elif player == 4 and computer == 3:
  print("The CPU won!")
elif player == 4 and computer == 5:
  print("The player won!")
elif player == 5 and computer == 1:
  print("The player won!")
elif player == 5 and computer == 2:
  print("The CPU won!")
elif player == 5 and computer == 3:
  print("The player won!")
elif player == 5 and computer == 4:
  print("The CPU won!")
else:
  print("Enter a valid number.")