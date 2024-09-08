# Name: Akshaj Shrotri, 712973
# Description: This program is a math flashcards game. It is based off the very
#              popular movie 'Pirates of the Caribbean'. This game has multiple
#              levels that increase by difficulty. Additionally, this game has
#              options that the user can select to make the game harder. For
#              example, having limited amount of lives, and integer division.


# importing modules, tkinter and random
from tkinter import ttk
from tkinter import *
from tkinter import scrolledtext
import random
from tkinter.ttk import Checkbutton
from tkinter import messagebox

# Setting up the window
window = Tk()
window.title("Math Flashcards Game")

window.geometry('1024x768')

# Setting up tab control and setting up different tabs. One for game, and
# one for options and log
tab_control = ttk.Notebook(window)

tab1 = Frame(tab_control)
tab_control.add(tab1, text='Game')

# Creating a label for what level the user chooses on the options tab
tab2 = Frame(tab_control)
tab_control.add(tab2, text=' Options/Log ')
# Uploading images to the code

img2 = PhotoImage(file='plus.png')
img3 = PhotoImage(file="equal_sign.png")
img5 = PhotoImage(file="potc_backg.png")

# tab 1

# setting background for game tab
back_1 = Label(tab1, image = img5)
back_1.place(x=0,y=0)

# Creating a label for how many lives
lives = Label(tab1,  text="Number of Lives: Infinite",\
              font=("Pieces of Eight", 20), bg="#F4D499")
lives.place(x=650, y=530)


# spinbox for how many lives

var3 = IntVar() 

spin1 = Spinbox( tab1, from_ = 0, to = 10, width = 20, textvariable = var3)
spin1.place(x=700, y=600)

# Creating a checkbutton if the user would like to have lives in the game
lives_state = BooleanVar()
lives_state.set(False) #set check state

lives_choice = Checkbutton(tab1, text="Check to play with lives",\
                           var = lives_state, command=clicked_lives)
lives_choice.place(x=700,y=650)

# Skull 1
global img_lbl
img_lbl = Label(tab1, text="$",font=("Pieces of Eight", 50), bg="#F4D499")
img_lbl.place(x=525, y=150)

# skull 2
global operator
operator = Label(tab1, text="$",font=("Pieces of Eight", 50),bg="#F4D499")
operator.place(x=325, y=150)

# skull 3
global img_lbl2
img_lbl2 = Label(tab1, text="$",font=("Pieces of Eight", 50), bg="#F4D499")
img_lbl2.place(x=100, y=150)

# start button
start_btn = Button(tab1, text="Start", width = 20, font=("Pieces of Eight", 20)\
                   , command=start, bg="#F4D499")
start_btn.place(x=350,y=70)

# equal sign
equal_s = Label(tab1, text="=", font=("Arial",40), bg="#F4D499")
equal_s.place(x=680,y=160)

# Quit button

quit1 = Button(tab1, text="Quit", width = 20, font=("Pieces of Eight",15)\
               , command=quited, bg="#F4D499")
quit1.grid(row=1, column=8)

# Entry box 
entry = Entry(tab1, width=4,font=("Pieces of Eight", 50), bg="#F4D499")
entry.place(x=780, y=150)
entry.bind("<Return>", checked)

# Check mark
info = Label(tab1, text="Press enter to check!", \
             font=("Pieces of Eight",25), bg="#835211", fg="White")
info.place(x=620
           , y=280)

# Score

score = Label(tab1, text="Score", font=("Pieces of Eight",20), bg="#F4D499")
score.place(x=100, y=515)

# correct (score)
corrected = Label(tab1, text="Correct: ", font=("Pieces of Eight",15), \
                  bg="#F4D499")
corrected.place(x=90, y=580)

# wrong (score)
wrong = Label(tab1, text="Wrong: ", font=("Pieces of Eight",15), bg="#F4D499")
wrong.place(x=90, y=630)

# total (score)
total = Label(tab1, text="Total: ", font=("Pieces of Eight",20), bg="#F4D499")
total.place(x=90, y=680)

# reset button
reset_btn = Button(tab1, text="Reset", width = 20, font=("Pieces of Eight",15),\
                   bg="#F4D499", command=reset)
reset_btn.grid(row=1, column=7)

tab_control.pack(expand=1, fill='both')

# Help tab/button

help_btn = Button(tab1,  text="Help/Instructions", width = 20, \
                  font=("Pieces of Eight",15),bg="#F4D499", command=helped)
help_btn.place(x=750,y=0)

# Tab 2 (options/log)
back_2 = Label(tab2, image = img5)
back_2.place(x=0,y=0)

# choose level label

level_choose = Label(tab2, text="Level Chosen:?", \
                     font=("Pieces of Eight",30),bg="#F4D499")
level_choose.place(x=70,y=60)

# Creating a checkbox function for integer division
div_integer_state = BooleanVar()
div_integer_state.set(False) #set check state

div_integer = Checkbutton(tab2, text="Check to play with Integer Division",\
                          var = div_integer_state)
div_integer.place(x=70,y=525)

# creating all global variables
global lvl
global lvl1_check
global lvl2_check
global lvl3_check
global lvl4_check

# adding buttons for every level 
lvl1_check = Button(tab2, text="Random numbers between 1-3", \
                    font=("Pieces of Eight",15), command=clicked1, bg="#F4D499")
lvl1_check.place(x=50,y=150)

lvl2_check = Button(tab2, text="Random numbers between 1-6",\
                    font=("Pieces of Eight",15), command=clicked2, bg="#F4D499")
lvl2_check.place(x=50,y=250)

lvl3_check = Button(tab2, text="Random numbers between 1-9", \
                    font=("Pieces of Eight",15),command=clicked3, bg="#F4D499")
lvl3_check.place(x=50,y=350)

lvl4_check = Button(tab2, text="Random numbers between 1-12", \
                    font=("Pieces of Eight",15),command=clicked4, bg="#F4D499")
lvl4_check.place(x=50,y=450)

# Decision label

decision = Label(tab1, text="Decision", font=("Pieces of Eight",30),\
                 bg="#F4D499")
decision.place(x=380,y=350)

# scrolled text for the log 

scroll = scrolledtext.ScrolledText(tab2, width=40, height=20, bg="#F4D499")
scroll.place(x=500, y=175)
scroll.configure(state="disabled")

log_label = Label(tab2, text="Log: ", font=("Pieces of Eight",30), bg="#F4D499")
log_label.place(x=750, y=60)

# Adding labels for equations
log_eqn = Label(tab2, text="Previous Question:", \
                font=("Pieces of Eight",12), bg="#F4D499")
log_eqn.place(x=530, y=140)

# adding a decision label
r_or_n = Label(tab2, text="Decision:", \
               font=("Pieces of Eight",12), bg="#F4D499")
r_or_n.place(x=720, y=140)

# running program
window.mainloop()
