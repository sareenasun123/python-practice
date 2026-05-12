import random

'''
computer -- user
R -- P
P -- S
S --R

'''
data = ['r','p','s']
while True:
    computer = random.choice(data)
    user = input("Enter a value r,p,s:").lower()
    if user not in data:
        print("Invalid input choose r, p, s")
        continue

    if computer == user:
        print("Tie")

    elif(
        (computer == "r" and user == "p")
        or (computer == "p" and user == "s")
        or (computer == "s" and user == "r")
    ):
        print("You win!")
    else:
        print("You lost!")

    user_input = input("Do you want to play again y/n?").lower()
    if user_input == "n":
        break


