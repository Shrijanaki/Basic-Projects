import random
import time

fruits = ['apple', 'orange','strawberry','raspberry','banana']
vegetables = ['carrot','potato','beans','beetroot','brinjal']
stationery = ['pen','pencil','eraser','stapler','sharpner']

category = str(input("What category do you choose?"))
word = ''
guess = ''

if category == 'fruits':
    word += random.choice(fruits)
elif category == 'vegetables':
    word += random.choice(vegetables)
else:
    word += random.choice(stationery)
    
correct_guesses = 0
wrong_guesses = 0

turns = 5
for char in range(turns):
    char = str(input("Guess a letter:"))
    if char in word:
        print('correct')
        correct_guesses += 1
    else:
        print('wrong')
        wrong_guesses += 1
answer = str(input("Do you want to guess the word?"))        
time.sleep(0.5)            
print("And the word is...",word)
if answer == word:
    print("You win!")
else:
    print("You lose!")

    