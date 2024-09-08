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

# Creating functions for the level buttons so that it gets updated.
# This applies to clicked2, 3, and 4.
def clicked1():
    global level
    level = 1 # Creating a new variable for the checked function
    level_choose.configure(text="Level 1 Was Selected!",\
                         font=('Pieces of Eight',25), bg="#F4D499")

def clicked2():
    global level
    level = 2
    level_choose.configure(text="Level 2 Was Selected!",\
                         font=('Pieces of Eight',25), bg="#F4D499")

def clicked3():
    global level
    level = 3
    level_choose.configure(text="Level 3 Was Selected!",\
                         font=('Pieces of Eight',25), bg="#F4D499")
    
def clicked4():
    global level
    level = 4
    level_choose.configure(text="Level 4 Was Selected!",\
                         font=('Pieces of Eight',25), bg="#F4D499")

# function will update the label how many lives the user has choosen
def clicked_lives():
    lives.configure(text="Number of Lives: "+str(var3.get()),font=("Pieces of Eight", 20), bg="#F4D499")

# creating a start function that will be used for the start button
def start():
    # setting global variables so that it can be acessed in the function
    global level
    global num_1
    global num_2
    global sign
    global answer
    
    # Based off the clicked function, this will generate random numbers from
    # a set of random integers.
    if level == 1:
        num_1 = random.randint(1, 3)
        num_2 = random.randint(1, 3)
        
    elif level == 2:
        num_1 = random.randint(1, 6)
        num_2 = random.randint(1, 6)
    
    elif level == 3:
        num_1 = random.randint(1, 9)
        num_2 = random.randint(1, 9)
    
    else:
        num_1 = random.randint(1, 12)
        num_2 = random.randint(1, 12)
    
    # Creating a set of signs so that the function will only use these signs
    operator_list = ["+", "-", "×"]
    sign = random.choice(operator_list) # randomly choosing signs
    
    # Ff the integer division checkbox is selected, then it will also add the
    # option of integer division '//'
    if div_integer_state.get() == 1:
        operator_list =  ["+", "-", "×", "//"]
        sign = random.choice(operator_list) # randomly choosing signs
            
    # Based off the information above, if the sign choosen, it will use that
    # operation and 2 random numbers to create a variable that will become
    # the answer.
    if sign == "+":
        answer = num_1 + num_2    
    
    elif sign == "-":
        answer = num_1 - num_2    
    
    elif sign == "x":
        answer = num_1 * num_2
    
    elif sign == "//":
        answer = num_2 // num_1
        
    # Every time, it will update new numbers and signs using configure
    img_lbl.configure(text=num_1)
    operator.configure(text=sign, font=("Arial",50))
    img_lbl2.configure(text=num_2)

# creating a function for checking the answer from the entrybox
def checked(event):
    # Setting global variables so that it can be acessed in the function
    global level
    global num_1
    global num_2
    global sign
    global answer
    global correct
    global incorrect
    global atemp_made
    global num_lives
    global lives_state
    
    # Fixing the issue of negative numbers when subtracting
    if sign == "-":
        if num_2 < num_1:
            answer *= -1
        elif num_2 > num_1:
            answer *= -1
    else:
        answer *= 1
    
    # making sure that the spinbox number is greater than 0
    if var3.get() < 0:
        messagebox.showinfo('Error!', \
            'Please enter a number greater than 0!')
    else:
        pass
    # When the lives checkbox is clicked, it will run the if block     
    if lives_state.get() == 1:
        if var3.get() == incorrect: # if the lives is equal to amount of
                                    # incorrect, it will give a error message.
            messagebox.showinfo('Error!', \
            'You ran out of lives. Please click restart to restart the game!')
    
    else: # otherwise, this will just go through
        pass
    
    # Making sure that the entry box is a valid integer, if not, it will
    # ask the user to provide valid input using configure.
 
    if entry.get() != int:
        decision.configure(text="Please enter a valid integer!",\
                           font=("Pieces of Eight", 20), fg="red")
    else:
        pass    
    
    # Using if block to validate that the input given from the entrybox is
    # correct by the answer variable determined from above functions.
    if int(entry.get()) == answer:
        indication = "CORRECT"
        
        #Adds 1 to correct and attempted variables so that there is a runnning
        # total.
        correct += 1
        atemp_made += 1
        
        #Configures label to show the user that their entry was correct.
        corrected.configure( text="Correct:" + str(correct))
        decision.configure(text="Correct!", fg="green")
        c_or_w = "Correct!"
        
    else:

        #Adds 1 to incorrect and attempted variables so that there is a runnning
        # total.
        incorrect += 1
        atemp_made += 1
        
        #Configures label to show the user that their entry was wrong.
        wrong.configure( text="Wrong:" + str(incorrect))
        decision.configure(text="Wrong!", fg="red")
        c_or_w = "Wrong!"
        
        
        #Configures label to current atemp_made value.
    total.configure( text="Total:" + str(atemp_made))
   
    
    #Deletes previous user input in text box.
    entry.delete(0, END)

    # Generates the list of operators again so that the operators are chosen'
    # after the user has made input.
    
    operator_list = ["+", "-", "×"]
    sign = random.choice(operator_list)
    if div_integer_state.get() == 1:
        sign =  ["+", "-", "×", "//"]
        sign = random.choice(operator_list)
    
    # Based off the information above, if the sign choosen, it will use that
    # operation and 2 random numbers to create a variable that will become
    # the answer. The exact same as the start function.
    if sign == "+":
        answer = num_1 + num_2    
    elif sign == "-":
        answer = num_1 - num_2    
    elif sign == "x":
        answer = num_1 * num_2
    elif sign == "//":
        answer = num_2 // num_1


    # Based off the clicked function, this will generate random numbers from
    # a set of random integers. The exact same as the start function.
    if level == 1:
        num_1 = random.randint(1, 3)
        num_2 = random.randint(1, 3)

    elif level == 2:
        num_1 = random.randint(1, 6)
        num_2 = random.randint(1, 6)
    
    elif level == 3:
        num_1 = random.randint(1, 9)
        num_2 = random.randint(1, 9)
    
    else:
        num_1 = random.randint(1, 12)
        num_2 = random.randint(1, 12)
    
    # This will add to the scrolledtext variable acting as a log, so that the
    # user can see what previous questions they have done.
    scroll.configure(state="normal")
    scroll.insert(INSERT, str(num_2) + " " + str(sign) + " " + str(num_1)\
                  +"               "+str(c_or_w)+"\n")
    scroll.configure(state="disabled")
    
    # Based off the information above, if the sign choosen, it will use that
    # operation and 2 random numbers to create a variable that will become
    # the answer. The exact same as the start function.
    if sign == "+":
        answer = num_1 + num_2
        
    elif sign == "-":
        answer = num_1 - num_2
        
    else:
        answer = num_1 * num_2

    # Every time, it will update new numbers and signs using configure.
    # The exact same as the start function.
    img_lbl.configure(text=num_1)
    operator.configure(text=sign, font=("Arial",50))
    img_lbl2.configure(text=num_2)    

# This function is called if the quit button is pressed, which will quit the
# entire program.
def quited():
    window.destroy()

# This function is called if the reset button is pressed, which will reset the
# entire program and all of the variables.     
def reset():
    # creating variables global so that they can be accessed in the function
    global level
    global num_1
    global num_2
    global sign
    global answer
    global correct
    global incorrect
    global atemp_made
    global spin1
    global lives
    
    #Deletes user input in textbox and restarts the entrybox.
    entry.delete(0, END)
    
    #Sets the values of variables to 0, which will reset everything.
    level = ()
    num_1 = ()
    num_2 = ()
    sign = ()
    answer = ()
    correct = 0
    incorrect = 0
    atemp_made = 0
    
    # This will reset the scrolledtext widget, which in this case is the log.
    scroll.configure(state="normal")
    scroll.delete(0.0, END)
    scroll.configure(state="disabled")
    
    # Setting the operators back to basics.
    img_lbl.configure(text="$",font=("Pieces of Eight", 50))
    operator.configure(text="$",font=("Pieces of Eight", 50))
    img_lbl2.configure(text="$",font=("Pieces of Eight", 50))
    decision.configure(text="Decision", font=("Pieces of Eight",30),fg="black")
    
    #Configures to show user no level has been chosen.
    level_choose.configure(text="Level Chosen:?", font=('Pieces of Eight',25)\
                           ,bg="#F4D499")
    
    #Configures labels to reset the score of the user.
    corrected.configure( text="Correct:" + str(correct))
    wrong.configure( text="Wrong:" + str(incorrect))
    total.configure( text="Total:" + str(atemp_made))
    
    # Making the lives label reset to 0
    lives.configure(text="Number of Lives: Infinite",\
              font=("Pieces of Eight", 20))
    var3.set(0) # setting the spinbox value to 0

#Help function, which if pressed, will give all of the instructions to the game
def helped():
     messagebox.showinfo('Help',\
                'Ahoy!, welcome to the Pirates of the Carabbean Game! \n\n'\
        'There are 4 levels that can be played: \n\n'
        'Level 1: Random Numbers between 1 and 3 \n'
        'Level 2: Random Numbers between 1 and 6 \n'
        'Level 3: Random Numbers between 1 and 9 \n'
        'Level 4: Random Numbers between 1 and 12 \n\n'
        'To check your answer, press the enter key on your keyboard. \n\n'
        'You can also choose how many lives you would like. \n'
        'If it is not selected, there will be infinite lives.\n\n'
        'Till later my friend!')
      
        
          

# initializing variables
level = ()
num_1 = ()
num_2 = ()
sign = ()
answer = ()
correct = 0
incorrect = 0
atemp_made = 0


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
corrected = Label(tab1, text="Correct: ", font=("Pieces of Eight",15), bg="#F4D499")
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

help_btn = Button(tab1,  text="Help/Instructions", width = 20, font=("Pieces of Eight",15),\
                   bg="#F4D499", command=helped)
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

div_integer = Checkbutton(tab2, text="Check to play with Integer Division",var = div_integer_state)
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