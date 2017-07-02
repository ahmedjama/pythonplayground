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
no_matter_what = "no matter what"
hexi = 8

print "Let's talk about %s." % name
print "He's %u centimeters tall." % height_in_cm # Changed format symbol to %u
print "He's %d kilograms heavy." % weight_in_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usally %s depending on the coffee." %teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get get %d." % (
    age, height_in_cm, weight_in_kg, age + height_in_cm + weight_in_kg
)

# Try more format characters. %r is a very useful one.
# It's like saying "print this no matter what."

print "Print this %r" % no_matter_what

print "The number 8 in hexidecimal is %x", % hexi
