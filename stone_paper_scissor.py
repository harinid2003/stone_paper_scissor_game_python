import random

rock = 0

paper = 1
scissor = 2
user_choice = int(input("Enter a num(0 or 1 or 2): "))
if user_choice>=3 or user_choice<0:
    print('invalid input you lose')
else:
    print(user_choice)
    comp_choice = random.randint(0, 2)
    print(comp_choice)
    if (
            user_choice == 1 and comp_choice == 1 or user_choice == 2 and comp_choice == 2 or user_choice == 0 and comp_choice == 0):
        print('draw')
    elif (user_choice == 0 and comp_choice == 2):
        print('You lose')
    elif (user_choice == 2 and comp_choice == 0):
        print('you win')
    elif (user_choice > comp_choice):
        print('you win')
    else:
        print('You lose')
