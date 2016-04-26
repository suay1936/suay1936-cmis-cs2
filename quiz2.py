#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) 22 == 22 #point
#b) 22 == 34 #point
#c) 8 > 5 and 5 > 3 #point
# 
#2) What does 'return' do?
# Return executes the function that has been defined in the function definition with the def #point
#
#
#
#3) What are 2 ways indentation is important in python code?
#a) It tells that the indented portion is part of the defined function #point
#b) It tells the program when to run the code eg. you define a function and the indented in return will produce the output of the defined function #point
#
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a) 36 #no point
#problem1_b) root 3 #no point
#problem1_c) 0 #point
#problem1_d) -5 #point
#
#problem2_a) True #point
#problem2_b) False #point
#problem2_c) True #no point
#problem2_d) False #no point
#
#problem3_a) 0.3 #point
#problem3_b) 0.5 #point
#problem3_c) 1 #no point
#problem3_d) 0.5 #point
#
#problem4_a)
#problem4_b)
#problem4_c)
#problem4_d)
#


#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)


import math

def numRange(a, b, c):
    
    if a > b and a > c:
        return a
    elif b > a and b> c:
        return b
    elif c > a and c > b:
        return c
    elif a = b = c or a = b 
        print ("You didn't follow the directions")       
    elif a = c or b = c
        print ("You didn't follow the directions")

def main(): 
    a= raw_input("Type in the first number ")
    b= raw_input("Type in the second number ")
    c= raw_input("Type in the third number ")


main()
# 23 25 26 
