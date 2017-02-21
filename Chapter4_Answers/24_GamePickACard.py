#Program to find a random card picked from a deck of cards
import random

#generate a number from 0 to 51
num = random.randint(0, 51)
card =""

#Find the value of the card 
if num % 13 == 0:
    card += "Ace of "
elif num % 13 == 10:
    card += "Jack of "
elif num % 13 == 11:
    card += "Queen of "
elif num % 13 == 12:
    card += "King of "
else:
    card += str(num % 13) + " of "

#Find the type of card
if num // 13 == 0:
    card += "Clubs"
elif num // 13 == 1:
    card += "Diamonds"
elif num // 13 == 2:
    card += "Hearts"
elif num // 13 == 3:
    card += "Spades"

print("The card you picked is", card)    