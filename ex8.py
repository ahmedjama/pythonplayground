#!/usr/bin/env python

# Exercise 8: Printing, Printing

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "\n Forever we remain oblivious to the future, \n",
    "lost to the past and enduring our torture, \n",
    "Forever we take chances to settle our scores, \n",
    "losing some battles and winning some wars. ... \n",
))