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

from tkinter import *
import random
import sys
import os

answers = ["Go for it!", "No way, Jose!", "I'm not sure, ask me again.",
           "Fear of the unknown is what imprisons us.", "It would be madness to do that!",
           "Only you can save mankind!", "Whatever.", "Yes, I think on balance that is the right choice.", "The chances are high!", "Computer says no...", "My sources say no", "Outlook not so good", "Very doubtful", "You can do it!", "It is certain", "It is decidedly so", "Without a doubt", "Yes definitely"]


def result():
    Label(root, text=random.choice(answers), font='Courier 10 bold', fg='white', bg='black').pack()
    Label(root, text='I hope you got the answer you wanted!',
          font='Courier 10 bold', fg='white', bg='black').pack()
    play_or_quit()


def shaking(event):
    Label(root, text="shaking ...\n" * 4, font='Courier 15 bold', fg='white', bg='black').pack()
    root.after(2000, result)


def empty(event):
    question.delete(0, 'end')


def play_or_quit():
    replay = Button(root, text='Play Again')
    replay.pack()
    replay.bind('<Button-1>', restart)
    Label(root, text='or', font='Courier 10 bold', fg='white', bg='black').pack()
    quit = Button(root, text='Quit', command=root.destroy)
    quit.pack()
    quit.bind('<Button-1>')


def restart(event):
    magic = sys.executable
    os.execl(magic, magic, * sys.argv)


root = Tk()
root.title('MAGIC 8 BALL')
root.configure(background='black')

Label(root, text='Welcome to the Magic 8 Ball', font='Courier 15 bold', fg='white', bg='black').pack()
Label(root, text='Please enter your question below',
      font='Courier 10', fg='white', bg='black').pack()

question = Entry(root, width=40)
question.pack()

submit = Button(root, text='Submit')
submit.pack()
submit.bind('<Button-1>', shaking)

clear = Button(root, text='Clear')
clear.pack()
clear.bind('<Button-1>', empty)


root.mainloop()
