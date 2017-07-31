###Dice roller

print "How many dice would you like to roll?"

dice = raw_input()
dice = int(dice)

if dice <= 0:
    print "Error! Please enter a positive number of dice."
    elif type(dice) == str:
        print "Error! Please enter a positive number of dice."
    else:
        print "Ok, I will roll %s dice." % (dice)

print "How many sides should each dice have?"

sides = raw_input()
sides = int(sides)

if sides <= 0:
    print "Error! Please enter a positive number of sides."
    elif type(sides) == str:
        print "Error! Please enter a positive number of sides."
    else:
        print "Ok, rolling %s sided dice." % (sides)

roll = 0

for roll in range(1, dice):
    roll = random.randint(1, sides)
    print roll
