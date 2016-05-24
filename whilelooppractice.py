#while  True:  #infinite smiley faces
    #print ";)",

#while False: #no smiley faces
    #print ";)"

a = 10
while a >= 0:
    print a
    a -= 1

def countdown(b):
    while b >= 1:
        print b
        b -= 1

def countup(c):
    while c < 34:
        print c
        c += 2 



def count(d):
    while d > 0:
        print d 
        d -= 1
    while d < 0:
        print d
        d += 1
    while d == 0:
        print " " 


def main():
    countdown(12)
    countup(12)
    count(10)
main()

