"""
Python 2 - Guess the Number

"""
import random
## GENERATE A RANDOM NUMBER BETWEEN 1 - 9
generated = random.randint(1, 9) 
##print(F"The Generated Number is {generated}")
## ASK THE USER TO GUESS THE GENERATED NUMBER
guessed = int(input('Human! Guess a number between 1 and 9: '))
## COMPARE THE USER'S GUESSED NUMBER WITH THE GENERATED NUMBER
while guessed != generated: ## KEEP TRYING GUESSING THE NUMBER UNTILL IT IS CORRECT
    if guessed < generated: ## IF THE GUESSED NUMBER IS LOWER THEN ASK FOR A HIGHER NUMBER
        guessed = int(input('Wrong! The answer is a HIGHER number: '))
    elif guessed > generated: ## IF THE GUESSED NUMBER IS HIGHER THEN ASK FOR A LOWER NUMBER
        guessed = int(input('Wrong! The answer is a LOWER number: '))
## IF GUESS IS CORRECT BREAK !
print('Correct, you guessed it !')