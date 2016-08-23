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
