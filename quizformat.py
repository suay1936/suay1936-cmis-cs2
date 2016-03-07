#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the sum of the areas, radiis, and diameters 
#of the 3 circles.
#Finally, it should produce output like this:
'''
Circle  Area    Diameter
c1      ...     ...
c2      ...     ...
c3      ...     ...
TOTALS  ...     ...
'''

# Hint: Radius is the square root of the area divided by pi
import math


#1 pt for header line
#3 pt for correct formula
#1 pt for return value
#1 pt for parameter name
#1 pt for function name
def radiusFromArea(area):
    radius = math.sqrt(float(area)/math.pi)
    return radius


#1pt for header line
#1pt for parameter names
#1pt for return value
#1pt for correct output format
#3pt for correct use of format function
def output(d1, d2, d3, sumDiameters):
    out = """
Circle    Diameter
c1        {}
c2        {}
c3        {}
Totals    {}
""".format(d1,d2,d3,sumDiameters)
    return out



#1pt header line
#1pt getting input
#1pt converting input
#1pt for calling output function
#2pt for correct diameter formula
#1pt for variable names

def main():
    #input
    c1 = float(raw_input("Area of C1: "))
    c2 = float(raw_input("Area of C2: "))
    c3 = float(raw_input("Area of C3: "))
 
   #processing
    r1 = radiusFromArea(c1)
    r2 = radiusFromArea(c2)
    r3 = radiusFromArea(c3)

    d1 = r1*2
    d2 = r2*2
    d3 = r3*2    
    sumDiameters = d1 + d2 + d3

    #output
    print output(d1,d2,d3, sumDiameters)


#1pt for calling main
main()

#1pt explanatory comments
#1pt code format
