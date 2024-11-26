# Adventure Game
name = input("Type Your Name: ")
print(f"Welcome, {name}, to this adventure!")

# Starting the adventure
answer = input("You are on a dirt road. It has come to an end, and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river. You can walk around it or swim across. Type 'walk' to walk around or 'swim' to swim across: ").lower()

    if answer == "swim":
        print("You swam across and were eaten by an alligator. Game Over!")
    elif answer == "walk":
        print("You walked around the river and reached the other side safely. You win!")
    else:
        print("Not a valid option. You lose!")

elif answer == "right":
    answer = input("You come to a bridge. It looks wobbly. Do you want to cross it or head back? Type 'cross' to cross it or 'back' to go back: ").lower()

    if answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? (yes/no): ").lower()

        if answer == "yes":
            print("You talked to the stranger, and they gave you gold. You win!")
        elif answer == "no":
            print("You ignored the stranger, and they felt offended. You lose!")
        else:
            print("Not a valid option. You lose!")
    elif answer == "back":
        print("You go back and lose your way. Game Over!")
    else:
        print("Not a valid option. You lose!")

else:
    print("Not a valid option. You lose!")
