def add (a, b):  # a and b are parameters 
	return a + b # this is the body of the function and it has to be tabbed in 4 spaces 
def msg_box (number):
    return "+" + ((len(number)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (number) + (2*" ") + "|" + "\n" + "+" + ((len(number) +4)*"-") + "+"
print msg_box ("7")

def sub (c, d):
    return c - d
def msg_box (number):
    return "+" + ((len(number)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (number) + (2*" ") + "|" + "\n" + "+" + ((len(number) +4)*"-") + "+"
print msg_box ("3") 

def mul (e, f):
	return e * f
def msg_box (number):
    return "+" + ((len(number)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (number) + (2*" ") + "|" + "\n" + "+" + ((len(number) +4)*"-") + "+"
print msg_box ("3")

def div (g, h):
	return g / h
def msg_box (number):
    return "+" + ((len(number)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (number) + (2*" ") + "|" + "\n" + "+" + ((len(number) +4)*"-") + "+"

import math #math is a module which is a file that contains a collection of related functions 
def hours_from_seconds (a):	#3600 is the number of seconds in one hour 
	return a / 3600
print hours_from_seconds (86400)
def msg_box (number):
    return "+" + ((len(number)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (number) + (2*" ") + "|" + "\n" + "+" + ((len(number) +4)*"-") + "+"
print msg_box ("24")

def circle_area (a):  #the equation for the area of a circle is pi(r^2) 
	return math.pi * (a**2)
print circle_area (5)  #brackets are used to call the function 
def msg_box (number):
    return "+" + ((len(number)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (number) + (2*" ") + "|" + "\n" + "+" + ((len(number) +4)*"-") + "+"
print msg_box ("78.5398163397")


def sphere_volume (a): #the equation for the volume of a sphere is (4/3)pi(r^3) 
	return 1.33333333333 * math.pi * (a**3)  #the 4/3 was changed to get a float answer a float number has to be put in
print sphere_volume (5)
def msg_box (number):
    return "+" + ((len(number)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (number) + (2*" ") + "|" + "\n" + "+" + ((len(number) +4)*"-") + "+"
print msg_box ("523.598775597")

def avg_volume (a, b):
	 return ((1.0/6 * math.pi * a**3) + (1.0/6 * math.pi * b**3)) /2
print avg_volume(10, 20)
def msg_box (number):
    return "+" + ((len(number)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (number) + (2*" ") + "|" + "\n" + "+" + ((len(number) +4)*"-") + "+"
print msg_box ("2356.19449019")



def area (a, b, c):	
    return math.sqrt (5.5*(5.5-a)*(5.5-b)*(5.5-c))
print area (3.0, 4.0, 5.0) #heron's formula 
def msg_box (number):
    return "+" + ((len(number)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (number) + (2*" ") + "|" + "\n" + "+" + ((len(number) +4)*"-") + "+"
print msg_box ("3.21130814467")



def right_align (word): #80 is the character width of the screen 
	return (80-len(word))*(" ")+word
print right_align ("Hello")


def center (word):  #40 is half the character width of the screen 
	return (40-len(word))*(" ")+word
print center ("Hello")


def msg_box (word): #here the built-in function len is used to make the box 
    return "+" + ((len(word)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (word) + (2*" ") + "|" + "\n" + "+" + ((len(word) +4)*"-") + "+" # \n is used to start a newline in the text 
print msg_box ("Hello")

def msg_box (word):
    return "+" + ((len(word)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (word) + (2*" ") + "|" + "\n" + "+" + ((len(word) +4)*"-") + "+"
print msg_box ("I eat cats!")
a= add (3, 4)  #brackets are used here to call the function so that it performs the operation generating a value 
n= msg_box ("7") 
print n
n= msg_box ("3")
print n
n= msg_box ("3")
print n
n= msg_box ("-1")
print n
n= msg_box ("-1")
print n
n= msg_box ("56")
print n
n= msg_box ("0.916666666667")
print n
n = msg_box ("0.92871428571")
print n
n= msg_box ("24")
print n
n= msg_box ("24")
print n
n= msg_box ("78.5398163397")
print n
n= msg_box ("78.5398163397")
print n
n= msg_box ("523.598775597")
print n
n= msg_box ("523.598775597")
print n
n= msg_box ("2356.19449019")
print n
n= msg_box ("2356.19449019")
print n
n= msg_box ("3.21130814467")
print n 
n= msg_box ("3.21130814467")
print n 



j= right_align ("Hello")
print j
j= right_align ("Hello")
print j
k= center ("Hello")
print k
k= center ("Hello")
print k
l= msg_box ("Hello")
print l
l= msg_box ("Hello")
print l
m= msg_box ("I eat cats!")
print m
m= msg_box ("I eat cats!")
print m

a= add (1,2)
print a
b= sub (3, 4)
print b
b= sub (5,6)
print b
c= mul (7, 8)
print c
c= mul (9, 10)
d= div (11.0, 12.0)
print d
d= div (13.0, 14.0)
print d 
e= hours_from_seconds (86400)
print e
e= hours_from_seconds (86400)
print e
f= circle_area (5)
print f
f= circle_area (5)
print f
g= sphere_volume (5)
print g
g = sphere_volume (5)
print g
h= avg_volume (10, 20)
print h
h= avg_volume (10, 20)
print h
i= area (3.0, 4.0, 5.0)
print i
i= area (3.0, 4.0, 5.0)
print i

