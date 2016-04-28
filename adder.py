
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
    
        
def adder(track):
    num = raw_input("num: ")
    if num == "":
        print "The sum of the numbers will be calculated"
    else:
        track += num
        print "Running total: {}".format(track)
        adder(trackgit )
        
        

def main():
    track = 0

    countdownfromto(10, 1) 
    countupfromto(5, 10)
    adder(track)
    
    return 

main()
 	



#code must ask the user to put in some numbers if the user doesn't put in a number and presses enter >> adder stop case then gives you the sum 
#to make recursion: function calls itself
#biggest 
#smallest
#pow
