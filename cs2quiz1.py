#Part 1:Terminology (13/15)
#Part 2:Programming (2/25)
#Total: (15/40)
#Part 1: Terminology (15 points) 
#1 1pt) What is the symbol "=" used for? (0)
# It is used to indicate that something is equal (the same) to the other. 
#
#
#2 3pts) Write a technical definition for 'function' (3)
# A function is an unambiguous step by step process that takes in a something (input) then processes it (the coding part) and spits out a value (output/ performing the computation). 
#
#
#3 1pt) What does the keyword "return" do? (1)
# The keyword return spits out a value from the function. 
#
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two (4)
#   examples of each below
#	1: str "Strawberry" "Banana"
#	2: int 7 9 
#	3: float 4.56 7.98
#	4: bool True False 
#	5: len len(Cookie) len(Oreos)
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"? (2)
# A function definition defines the function it describes what the function will do. Function call executes the function definition thus producing a value. 
#
#
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them (3)
#	1: input: something is put in lets say a number.
#	2: process: the program runs the value it does the calculation.
#	3: output: a value is given out the process is complete. 
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi

import math
def diameter_circle (a): 
        circle = raw_input("C1: ")
    return math.sqrt( a/ pi) * 2
def diameter_circle (b):        
        circletwo = raw_input("C2: ")
    return math.sqrt( b / pi) * 2
def diameter_circle (c):
        circlethree = raw_input("C3: ")
    return math.sqrt( c / pi) * 2
def add (a, b, c): 
    return str("a" + "b" + "c") 
print 
print 
print 

# 1 point for return value
# 1 point for parameter name 
# 
#



