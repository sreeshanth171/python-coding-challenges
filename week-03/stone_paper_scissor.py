import random
list = ["stone","paper","scissor"]
choise = input("enter your choice : ").lower()
computer = random.choice(list)
if choise == computer:
    print("draw","computer choose ",computer)
elif (computer == "scissor" and choise == "paper") or \
    (computer == "stone" and choise == "scissor") or \
    (computer == "paper" and choise == "stone"):
    print("you lose ","computer choose ",computer)
else:
    print("you win computer choose ",computer)
