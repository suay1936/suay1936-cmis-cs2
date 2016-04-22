def countdownfromto(start, stop):
    if start < stop:
        print "It's not going to work."    
    elif start == stop:
        print stop
    else:
        print start
        countdownfromto(start -1, stop)
    
        
    
        
countdownfromto(1, 10)    
    





































#adder stop case = print nothing then press enters gives your the sum
#running total use input
