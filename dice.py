"""Dice roller - rolls any number of dice with any number of sides"""
# random int generator
from random import randint


def main():
    """main function"""


if __name__ == "__main__":
    main()


def dice_input():
    """Get the number of dice."""
    # input for dice number variable
    dice = int(raw_input('How many dice would you like to roll? '))
    dice_check(dice)
    return dice


def sides_input():
    """Get the number of sides"""
    sides = int(raw_input('How many sides does each dice have? '))
    sides_check(sides)
    return sides


def roll_dice(dice, sides):
    """Loop through number of dice, randomly generate numbers"""
    print "Ok, rolling %s dice with %s sides." % (dice, sides)
    roll = 0
    for roll in range(0, dice):
        print "[%s]" % (randint(1, sides))

    again = raw_input('Would you like to roll, make a change, or end r/c/e? ')
    
    if again == 'r':
        roll_dice()
    elif again == 'e':
        print "Ok, thanks!"
        return
    elif again == 'c':
        change()
    else:
        print "Please respond with r, c, or e"
        roll_dice()


def dice_check(dice):
    """Check for positive integers"""
    dice_int = False
    while not dice_int:
        if dice <= 0:
            print "Error! Please enter a positive number of dice."
            dice_input()
        else:
            dice_int = True
            print "Ok, I will roll %s dice." % (dice)


def sides_check(sides):
    """Check for positive integers"""
    sides_int = False
    while not sides_int:
        if sides <= 0:
            print "Error! Please enter a positive number of sides."
            sides_input()
        else:
            sides_int = True


<<<<<<< HEAD
# def reroll():
#    """Ask user for reroll"""
#    again = raw_input('Would you like to roll, make a change, or end r/c/e? ')
#    if again == 'r':
#        roll_dice()
#    elif again == 'e':
#        print "Ok, thanks!"
#        return
#    elif again == 'c':
#        change()
#    else:
#        print "Please respond with r, c, or e"
#        reroll()
#    reroll()
=======
def reroll(dice, sides):
    """Ask user for reroll"""
    again = raw_input('Would you like to reroll, make a change, or end r/c/e? ')
    if again == 'r':
        roll_dice(dice, sides)
    elif again == 'e':
        print "Ok, thanks!"
        return
    elif again == 'c':
        change(dice, sides)
    else:
        print "Please respond with r, c, or e"
        reroll(dice, sides)
    reroll(dice, sides)
>>>>>>> 507a74c9f369e47b91422438df8675f7b7c807b2


def change(dice, sides):
    """Change number of dice or sides"""
    which = raw_input('Change dice or sides d/s? ')
    if which == 'd':
        dice_new = dice_input()
        roll_dice(dice_new, sides)
    else:
        if which == 's':
            sides_new = sides_input()
            roll_dice(dice, sides_new)
        else:
            print 'Please input only d or s'
            change(dice, sides)

<<<<<<< HEAD
dice_input()
sides_input()
roll_dice()
# reroll()
=======
dice = dice_input()
sides = sides_input()
roll_dice(dice, sides)
reroll(dice, sides)
>>>>>>> 507a74c9f369e47b91422438df8675f7b7c807b2
