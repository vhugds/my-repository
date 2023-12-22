import addition
from addition import add

import substraction
from substraction import substract

import division
from division import divide

import multiplication
from multiplication import multiply

print("please select operation.")
print("1. addition")
print("2.substraction")
print("3.division")
print("4.multiplication")

while True : 
     userchoice = input("select a number 1/2/3/4:")
     if userchoice in ('1','2','3','4'):
      
        num1=input("select first number:")
        num2=input("select second number:")
      
        if userchoice == '1':
         print(num1,"+",num2,"=",add(num1,num2))
        
        elif userchoice == '2':
          print(num1,"-",num2,"=",substract(num1,num2))
        
        elif userchoice == '3':
         print(num1,"/",num2,"=",divide(num1,num2))    
        
        elif userchoice == '4':
         print(num1,"*",num2,"=",multiply(num1,num2))
        
        nextcalculation =  input("i can help u with more calculation do you(yes/no):")
        if nextcalculation == "no":
         break
else:
 print("invalid input")
 