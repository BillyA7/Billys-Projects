'''[Project] Magic 8 Ball
Goal

I'm sure you've used a magic 8 ball at one point in your life. You ask it a question, turn it right side up and it gives an answer by way of a floating die with responses written on it. You can create one in python. You must:

Allow the user to enter their question

Display an in progress message( i.e. "thinking")

Create 20 responses, and show a random response

Allow the user to ask another question or quit

Bonus Using whatever module you like, add a gui. Your gui must have:

A box for users to enter the question

At least 4 buttons: Ask , clear(the text box), play again and quit(this must close the window)'''

import random
import time
import sys

answers = ["Go for it!", "No way, Jose!", "I'm not sure, ask me again.",
           "Fear of the unknown is what imprisons us.", "It would be madness to do that!", "Only you can save mankind!", "Whatever.", "Yes, I think on balance that is the right choice.", "The chances are high!", "Computer says no...", "My sources say no", "Outlook not so good", "Very doubtful", "You can do it!", "It is certain", "It is decidedly so", "Without a doubt", "Yes definitely"]


def shaking():
    print()
    print("shaking ...\n" * 4)
    time.sleep(1)
    print(random.choice(answers))
    print()
    time.sleep(1)
    print('I hope you got the answer you wanted\n')
    time.sleep(1)


def replay():
    another_go = input('Would you like to ask another question?\n').lower()
    print()
    if another_go == 'yes':
        input(f'Hello again {name}, please enter another question below:\n')
        time.sleep(1)
        shaking()
        replay()
    elif another_go == 'no':
        print(f'Thanks for playing {name}, bye!\n')
        time.sleep(2)
        sys.exit()
    else:
        print('We need a yes or no answer only please.\n')
        time.sleep(1)
        print('So I\'ll ask again.\n')
        time.sleep(1)
        replay()


print('Welcome to the Magic 8 Ball.\n')
time.sleep(2)
name = input('Please tell me your name:\n')
time.sleep(1)
print()
input(f'Hi there {name}, please enter your question below:\n')
time.sleep(1)
shaking()
replay()
