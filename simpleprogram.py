# simpleprogram: currency conversion
import math

def baht_to_dollar(dollar1):
    dollar1 = dollar1 / 35.63
  

def baht_to_pound(pound1):
    pound1 = pound1 / 50.94
   

def dollar_to_baht(baht1):
    baht1 = baht1 * 35.63
   

def dollar_to_pound(pound2):
    pound2 = pound2 * 0.70
  

def pound_to_baht(baht2):
    baht2 = baht2 * 50.94
   

def pound_to_dollar(dollar2):
    dollar2 = dollar2 * 1.44
    

def total_baht(baht1, baht2):
    return baht1 + baht2
  
def total_dollar(dollar1, dollar2):
    return dollar1 + dollar2
   
def total_pound(pound1, pound2):
    return pound1 + pound2 
    
def printing(baht3, dollar3, pound3): 
    will_print = """ I now have {} baht, {} dollars, and  {} pounds. """.format(baht3, dollar3, pound3)
    return will_print 
    

def main():

    #input section
    #baht to dollars and pounds
    dollar1 = raw_input("How much money do you have in baht?: ")
    pound1 = raw_input("Go do something with your money, how much money do you have in baht now?: ")
    # dollars to baht and pounds
    baht1 = raw_input("How much money do you have in dollars?: ")
    pound2 = raw_input("Go do something with your money, how much money do you have in dollars now?: ")  
    # pound to baht and dollars
    baht2 = raw_input("How much money do you have in pounds?: ")
    dollar2 = raw_input("Go do something with your money, how much money do you have in pounds now?: ")


    #processsing?
    baht3 = total_baht(float(baht1), float(baht2))
    dollar3 = total_dollar(float(dollar1), float(dollar2))
    pound3 = total_pound(float(pound1), float(pound2))

    will_print = printing(baht3, dollar3, pound3)
    print will_print 
    
#werk werk werk 
main()

