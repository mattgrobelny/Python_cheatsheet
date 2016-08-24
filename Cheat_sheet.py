###############################################################################
#
#  ,-----.          ,--.                       ,--.
# '  .--./ ,---.  ,-|  |,---.  ,---. ,--,--. ,-|  |,---. ,--,--,--.,--. ,--.
# |  |    | .-. |' .-. | .-. :| .--'' ,-.  |' .-. | .-. :|        | \  '  /
# '  '--'\' '-' '\ `-' \   --.\ `--.\ '-'  |\ `-' \   --.|  |  |  |  \   '
#  `-----' `---'  `---' `----' `---' `--`--' `---' `----'`--`--`--'.-'  /
#                                                                 `---'
#
# Code imported/summarized from https://www.codecademy.com
#
###############################################################################
# importing modules

from math import sqrt

# Import *everything* from the math module on line 3!
from math import *

###############################################################################
# Printing variable within a string

string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

g = "Golf"
h = "Hotel"
print "%s, %s" % (g, h)

###############################################################################
# Functions

def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print "With tax: %f" % bill
    return bill

def tip(bill):

    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print "With tip: %f" % bill
    return bill

meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)


###############################################################################
# finding type of variable

print type(42)
print type(4.2)
print type('spam')

###############################################################################
# Time and date

from datetime import datetime
now=datetime.now()
print '%s/%s/%s' % (now.month,now.day,now.year)

###############################################################################
# If statements

if x == 1:
    print "yes x == 1"
        #indent me!
    elif x == 2
    print "x is actually 2!"

###############################################################################
# Classes

class Animal(object):  # new class
    is_alive = True    # global variable for the class
    def __init__(self,name,size, breed ):    #pass in initializing Function
        self.name = name
        self.size = size
        self.breed = breed
    def desciption(self):
        print self.breed
        print self.name

zebra = Animal("Bob", 10, "pure")

print zebra.name        # prints Bob
print zebra.size        # prints 10
print zebra.breed       # prints pure

print zebra.is_alive    # prints True

print zebra.desciption()
