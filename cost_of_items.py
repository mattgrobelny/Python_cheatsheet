#!/usr/bin/python
# Write a program that determines the total cost of all items entered.
# Prompt the user for the initial cost of each item and add this cost to the total.
# Each item will be entered as a whole number (interger). For each item entered, display
# "Luxury Item" for each item that exceeds $500, and display "Sale Item" for each item
# entered that is divisible by 10. Finish asking for new items when value entered is 0.
# Following an entry of 0, display the total cost of all items, and the number of
# items purchased that are "Luxury", and "Sale".

total = 0
both = 0
while 1:
    item= raw_input('Item name?: ')
    if item == '0':
        print total, both
        break
    else:
        item_cost = int(raw_input('How much does the item cost? '))
        total = total + int(item_cost)
        if item_cost > 500 and item_cost % 10 == 0:
            print item_cost,"Lux and sale"
            both += 1
        elif item_cost > 500:
            print item_cost,"Lux"
        elif item_cost % 10 == 0:
            print item_cost,"sale"
