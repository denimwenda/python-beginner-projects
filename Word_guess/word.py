# Importing the module
import random

# Getting the user name and greeting the user.
name = input("What is your name? ")
print("Good Luck! , name")

# Lists of words and choosing a random word
words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'geeks']
word = random.choice(words)

# Prompt the user to guess
print("Guess the characters")

guesses = ''
turns = 12

while turns > 0:
    failed = 0
    
    for char in word:
        if char in guesses:
            print(char, end=" ")
            
        else:
            print("_")
            failed += 1
            
    if failed == 0:
        print("You win")
        print("The word is: ", word)
        break
    
    print()
    guess = input("guess character:")
    
    guesses += guess
    
    if guess not in word:
        
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')
        
        if turns == 0:
            print("You Loose")