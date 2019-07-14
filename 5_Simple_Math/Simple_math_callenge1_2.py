#-*- encoding: utf-8 -*-
from __future__ import print_function

number1 = raw_input("What is the first number ? ")
if number1.isdigit() == False: # number valid check
    print ("input value is only integer! ({})".format(number1))
    quit()
if int(number1) < 0: # is number positive check
    printf("input number is only positive number! ({})".format(number1))
    quit()

number2 = raw_input("What is the second number ? ")
if number2.isdigit() == False: # number valid check
    print ("input value is only integer! ({})".format(number2))
    quit()
if int(number2) < 0: # is number positive check
    printf("input number is only positive number! ({})".format(number2))
    quit()
    
number1 = int(number1)
number2 = int(number2)


if number2 < 0:
    printf("input number is only positive number! ({})".format(number1))
    quit()

print ("{n1} + {n2} = {ret1} \n{n1} - {n2} = {ret2} \n"
       "{n1} * {n2} = {ret3} \n{n1} \\ {n2} = {ret4} \n"
       .format(n1=number1, n2=number2, ret1=(number1 + number2), 
               ret2=(number1 - number2), ret3=(number1 * number2),
               ret4=(number1 / number2)))
