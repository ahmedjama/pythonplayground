#!/usr/bin/python
# Exercise 5: More Variables and Printing

name = 'Zed A. Shaw'
age = 35 # not a lie
height_in_inches = 74 # inches
height_in_cm = height_in_inches * 2.54 # cm
weight_in_lbs = 180 # lbs
weight_in_kg = weight_in_lbs * 0.453592 # kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'


print "Let's talk about %s." % name
print "He's %d inches tall." % height_in_cm
print "He's %d pinds heavy." % weight_in_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usally %s depending on the coffee." %teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get get %d." % (
    age, height_in_cm, weight_in_kg, age + height_in_cm + weight_in_kg
)
