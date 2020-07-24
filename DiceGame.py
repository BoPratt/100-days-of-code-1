# Dice program

# Generate random number dNum
# Print dNum in the form of a Die
# Ask user if they want to roll again and do so.

import random as r

play = 'y'

while (play == 'y'):
    dNum = r.randint(1, 7)
    print('|---------|')
    if(dNum == 1):
        print('|         |')
        print('|    o    |')
        print('|         |')
    elif (dNum == 2):
        print('|    o    |')
        print('|         |')
        print('|    o    |')
    elif (dNum == 3):
        print('| o       |')
        print('|    o    |')
        print('|       o |')
    elif (dNum == 4):
        print('| o     o |')
        print('|         |')
        print('| o     o |')
    elif (dNum == 5):
        print('| o     o |')
        print('|    o    |')
        print('| o     o |')
    else:
        print('| o     o |')
        print('| o     o |')
        print('| o     o |')
    print('|---------|')
    # print graphical die.
    play = input('Do you want to roll again? (y/n)')


print('Game Over. Thanks for Playing!')
