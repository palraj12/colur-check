#Type the colour and not the word
#from usingpython.com

#import the modules we need, for creating a GUI...
import tkinter
#...and for creating random numbers.
import random

#the list of possible colour.
colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown','lightgreen',"lightred',"lightblue"]
#the player's score, initially 0.
score=0
#the game time left, initially 30 seconds.
timeleft=60

#a function that will start the game.
def startGame(event):

    #if there's still time left...
    if timeleft == 30:
        #start the countdown timer.
        countdown()
        
    #run the function to choose the next colour.
    nextColour()
           
from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)
mainloop()


#function to choose and display the next colour.
def nextColour():

    #use the globally declared 'score' and 'play' variables above.
    global score
    global timeleft

    #if a game is currently in play...
    if timeleft > 0:

        #...make the text entry box active.
        e.focus_set()

        #if the colour typed is equal to the colour of the text...
        if e.get().lower() == colours[1].lower():
            #...add one to the score.
            score += 1

        #clear the text entry box.
        e.delete(0, tkinter.END)
        #shuffle the list of colours.
        random.shuffle(colours)
        #change the colour to type, by changing the text _and_ the colour to a random colour value
        label.config(fg=str(colours[1]), text=str(colours[0]))
        #update the score.
        scoreLabel.config(text="Score: " + str(score))

#a countdown timer function. 
def countdown():

    #use the globally declared 'play' variable above.
    global timeleft

    #if a game is in play...
    if timeleft > 0:

        #decrement the timer.
        timeleft -= 1
        #update the time left label.
        timeLabel.config(text="Time left: " + str(timeleft))
        #run the function again after 1 second.
        timeLabel.after(1000, countdown)
    
#create a GUI window.
root = tkinter.Tk()
#set the title.
root.title("TTCANTW")
redbutton.pack( side = LEFT)
greenbutton = Button(frame, text = 'Brown', fg='brown')
greenbutton.pack( side = LEFT )
bluebutton = Button(frame, text ='Blue', fg ='blue')
bluebutton.pack( side = LEFT )
blackbutton = Button(bottomframe, text ='Black', fg ='black')
blackbutton.pack( side = BOTTOM)
root.mainloop()
#set the size.
root.geometry("375x200")

#add an instructions label.
instructions = tkinter.Label(root, text="Type in the colour of the words, and not the word text!", font=('Helvetica', 12))
instructions.pack()

#add a score label.
scoreLabel = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack()

#add a time left label.
timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

#add a label for displaying the colours.
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

#add a text entry box for typing in colours.
e = tkinter.Entry(root)
#run the 'startGame' function when the enter key is pressed.
root.bind('<Return>', startGame)
e.pack()
#set focus on the entry box.
e.focus_set()

#start the GUI
root.mainloop()
