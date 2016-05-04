
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
        track += int(num)
        print "Running total: {}".format(track)
        adder(track)
        
def biggest(number):
    a = raw_input("Next number: ")
    if a == "":
    return number

    else: 
        a = float(a)
        if a > number:
            number = a
        return biggest(number)

def smallest(number):
    b = raw_input("Next number: ")
    if b == "":
    return number

    else: 
        b = float(b)
        if b > number:
            number = b
        return biggest(number)

def pow(x, n)
    if n == 0:
        return 1
    else:
        return x * pow(x, n-1)


def main():
    track = 0
    countdownfromto(10, 1) 
    countupfromto(5, 10)
    adder(track)
    
    

main()
 	



#code must ask the user to put in some numbers if the user doesn't put in a number and presses enter >> adder stop case then gives you the sum 
#to make recursion: function calls itself
#biggest 
#smallest
#pow
