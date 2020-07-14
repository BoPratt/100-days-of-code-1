import random as r
bank = 1000
chances = r.randint(1,5)

marbles = {1:'green', 2:'green', 3:'green', 4:'green', 5:'green', 6:'black', 7:'red', 8:'red', 9:'red', 10:'white'}
guess = ''
messageAlt = ''
messageAlt1 = 'The marble was '
#bet = int(input(f'You have {chances} tries. How much would you like to bet?'))
while(chances > 0):
    bet = int(input(f'{messageAlt1}\nCurent bank: ${bank}\nYou have {chances} tries. How much would you like to bet {messageAlt}?'))
    guess = marbles[r.randint(1,10)]
    if (guess == 'green'):
        bank+=bet
    elif (guess == 'black'):
        bank+=(bet*10)
    elif (guess == 'white'):
        bank-=(bet*5)
    else:
        bank-=bet
    if(bank <= 500):
        break
    messageAlt = 'this time'
    messageAlt1 = 'The marble was ' + guess + '!!!'
    chances-=1



print(f'Last marble was {guess}. GAME OVER....you have ${bank} left as you leave.')
