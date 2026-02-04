print("Welcome to Number Guessing Game")
print("I am thinking of a number between 1 and 100.")

import random
number=random.randint(1,100)
a = input("Choose a difficulty level: 'easy' or 'hard': ")



attempts=0

def easy():
    attempts=10
    while attempts > 0:
        guess = int(input("Make a guess:"))
        if guess < number:
            print('Too low.Try again.')

        elif guess == number:
            print("You found out the number which is",number)
            
            break 

        else:
            print('Too high.Try again')
        
        
        attempts -=1
        if attempts == 0:
            print('You ran out of the attempts')

easy()

def hard():
    
    attempts=5
    while attempts > 0:
        guess = int(input("Make a guess:"))
        if guess < number:
            print('Too low.Try again.')

        elif guess == number:
            print("You found out the number which is",number)
            
            break 

        else:
            print('Too high.Try again')
        
        
        attempts -=1
        if attempts == 0:
            print('You ran out of the attempts')

if a == 'easy':
    easy()
elif a == 'hard':
    hard()
else:
    print("Invalid choice")
