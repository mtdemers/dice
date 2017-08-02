###Dice roller
###random int generator
from random import randint 

###Get number of dice, assign global variable
def dice_input():
    global dice
    dice = int(raw_input('How many dice would you like to roll? ')) #input for dice number variable
    dice_check()
    return

###Get number of sides, assign global variable
def sides_input():
    global sides
    sides = int(raw_input('How many sides does each dice have? '))
    sides_check()
    return

###Loop through number of dice, print random number per sides
def roll_dice():
    print "Ok, rolling %s dice with %s sides." % (dice, sides)
    roll = 0
    for roll in range(0, dice):
        print("[%s]" % (randint(1,sides)))

def dice_check(): ###Check for positive int
    dice_int = False
    while not dice_int: 
        if dice <= 0: 
            print "Error! Please enter a positive number of dice."
            dice_input()
        else:
            dice_int = True
            print "Ok, I will roll %s dice." % (dice)

def sides_check(): ###Check for positive int
    sides_int = False
    while not sides_int: 
        if sides <= 0: 
            print "Error! Please enter a positive number of sides."
            sides_input()
        else:
            sides_int = True

###check to see if user would like to roll again
def reroll(): 
    again = raw_input('Would you like to reroll, make a change, or end r/c/e? ')
    if again == 'r':
        roll_dice()
    else:
        if again == 'e':
            print "Ok, thanks!"
            return
        else:
            if again == 'c':
                change()
            else:
                print "Please respond with y or n"
                reroll()
    reroll()

###Change number of dice or sides
def change():
    which = raw_input('Change dice or sides d/s? ')
    if which == 'd':
        dice_input()
        roll_dice()
    else:
        if which == 's':
            sides_input()
            roll_dice()
        else:
            print 'Please input only d or s'
            change()


dice_input() ###Get number of dice
sides_input() ###Get number of sides
roll_dice()
reroll()