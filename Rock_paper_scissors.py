import random

user_wins=0
system_wins=0

option=['rock','paper','scissors']

while True:
    user_input=input('Tpe Rock/Paper/Scissors Or Q to quit.').lower()
    if user_input=='q':
        break
    if user_input not in option:
        continue
    random_number=random.randint(0,2)
    #rock:0   paper:1    scissors:2
    computer_quess=option[random_number]
    print('Computer Picked',computer_quess+".")

    if user_input=='rock' and computer_quess=='scissors':
        print('You Own')
        user_wins+=1
    elif user_input=='paper' and computer_quess=='rock':
        print('You Won')
        user_wins+=1
    elif user_input=='scissors' and computer_quess=='paper':
        print('You Won')
        user_wins+=1
    else:
        print('You Lost')
        system_wins+=1

print('You Won',user_wins,'times.')
print('The System Won',system_wins,'times.')
print('Good Byee!!')
