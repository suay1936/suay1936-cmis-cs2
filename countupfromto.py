def countupfromto(start, stop):
    if start > stop:
        print "Oops! Sorry, it won't work."
    elif start == stop:
        print start
    else:
        print start
        countupfromto(start +1, stop)

countupfromto(10, 5)




