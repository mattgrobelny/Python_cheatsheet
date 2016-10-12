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

def Pythagorean(a, b):
    c = a**2 + b**2
    return sqrt(c)

###############################################################################
# finding type of variable

print type(42)
print type(4.2)
print type('spam')

###############################################################################
# Time and date

from datetime import datetime
now = datetime.now()
print '%s/%s/%s' % (now.month, now.day, now.year)

###############################################################################
# If statements

if x == 1:
    print "yes x == 1"
    # indent me!
    elif x == 2
    print "x is actually 2!"

###############################################################################
# Classes

class Animal(object):  # new class
    is_alive = True    # global variable for the class

    def __init__(self, name, size, breed):    # pass in initializing Function
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

###############################################################################
# New stuff from IB501

# Need to know how to execute commands outside of python <-

###############################################################################
# For loops

for x in range(0, 3):
    print "We're on time %d" % (x)

###############################################################################
# If else
x = 2
if x == 10:
    print "yes x is equal to 10"
elif x == 5:
    print "x is:%s" % (x)
else:
    print x

###############################################################################
# While loops
for a in range(1, 11):
    print "here is a number: %s" % (a)
    while a == 10:
        print "got to %s !" % (a)
###############################################################################
# Dictionaries

# similar to array list of values, transported together
# Empty dictionary
foo = {}
foobar = {'id1': "ATCG", 'id2': "TGCA", 'id3': "TGAA"}
bar = {"good": 0, "bad": 1}

# refering to dic
print foobar['id1']

# containing arrays

# checking for keys
key = 'id1'

for key in foobar:
    print foobar[key]

pops = {}

pops['pop1'] = 35

pops['pop2'] = 36

pops['pop3'] = 72

print "sample count for pop3:", pops['pop3']

for key in pops:
    print pops[key]
    print key

# all dictionary values
print pops.values()
print pops.keys()

print pops.items()

# $ [72, 36, 35]
# $ ['pop3', 'pop2', 'pop1']
# $ [('pop3', 72), ('pop2', 36), ('pop1', 35)]

###############################################################################
# objects

class pop(object):
    """docstring for """
    def __init__(self, arg, name):
        super(, self).__init__()
        self.arg = arg
        self.name = name

pop_new = pop(1, "Name")

print pop_new.name
pop_new.name = "New pop"

###############################################################################
# Command line options

import sys

for i in ARGV:
    print ARGV[i]
