import random
num1 = random.randint(1, 13)
num2 = random.randint(1, 4)

cardnum1 = ''
cardnum2 = ''

input("<<<<Press the enter key to generate a card>>>>")

if True:
    if num1 == 11:
        cardnum1 = "Queen"
    elif num1 == 12:
        cardnum1 = "Jack"
    elif num1 == 13:
        cardnum1 = "King"
    elif num1 == 1:
        cardnum1 = "Ace"
    elif 1 < num1 < 10:
        cardnum1 = (num1)

if True:
    if num2 == 1:
        cardnum2 = "Spades"
    elif num2 == 2:
        cardnum2 = "Hearts"
    elif num2 == 3:
        cardnum2 = "Diamonds"
    elif num2 == 4:
        cardnum2 = "Clubs"

print((cardnum1), 'of', (cardnum2))