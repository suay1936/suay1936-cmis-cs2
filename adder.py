
def countdownfromto(start, stop):
    if start < stop:
        print "It's not going to work."    
    elif start == stop:
        print stop
    else:
        print start
        countdownfromto(start -1, stop)

countdownfromto(1, 10)      
        
def countupfromto(startA, stopA):
    if startA > stopA:
        print "Oops! Sorry, it won't work."
    elif startA == stopA:
        print startA
    else:
        print startA
        countupfromto(startA +1, stopA)

countupfromto(10, 5)
    
        
def adder():
    n = raw_input("n: ")
    if n == #conditional for when to stop the recursion and proceed to the sum
        pass  
        sum n 
    adder(): #function calls itself so that raw input is recursed 


def main():
    
    adder()
    countdownfromto(1, 10) 
    countupfromto(10, 5)
    
    return 

main()




#code must ask the user to put in some numbers if the user doesn't put in a number and presses enter >> adder stop case then gives you the sum
#pass makes it do nothing 
#to make recursion: function calls itself
