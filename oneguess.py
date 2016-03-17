# What is the minimum number? 5
# What is the maximum number? 10
# I'm thinking of a number from 5 to 10.
# What do you think it is?: 7

# The target was 9.
# Your guess was 7.
# That's under by 2.



#need to use the if an comparison
# interval comparison 

import random 
import math 


def sub(guess, target):
    return guess - target
def sub(guess, target):
    return target - guess


def main():
    minNumber = int(raw_input("What is the minimum number? "))
    maxNumber = int(raw_input("What is the maximum number? "))

    print "I'm thinking of a number from" 
    myNumberGuess = int(raw_input("What do you think it is?: "))
 
    def condition(guessTarget):
	
        if int(guess) > int(target) #needs work
   	        print "That's over by" 
            return sub(int(guess), int(target))
        elif int(guess) < int(target)
	        print "That's under by" sub(int(target), int(guess)) 
        else int(guess) == int(target):
             print "That's amazing! Someone's a lucky soul today!" 



main()
   
    
