from random import randint
import time
num = randint(0,2)
options = ["rock","paper","scissors"]
com_choice = options[num]
user_choice = raw_input("Enter your choice")
print str(com_choice)
print str(user_choice)
if user_choice == "rock":
    if com_choice == "rock":
        time.sleep(0.5)
        print("That's a tie!")
    elif com_choice == "paper":
        time.sleep(0.5)
        print("I win")
    else:
        time.sleep(0.5)
        print("You win")
elif user_choice == "paper":
    if com_choice == "rock":
        time.sleep(0.5)
        print("You win")
    elif com_choice == "paper":
        time.sleep(0.5)
        print("That's a tie!")
    else:
        time.sleep(0.5)
        print("I win!")
else:
    if com_choice == "rock":
        time.sleep(0.5)
        print("I win!")
    elif com_choice == "paper":
        time.sleep(0.5)
        print("you win!")
    else:
        time.sleep(0.5)
        print("That's a tie!")

