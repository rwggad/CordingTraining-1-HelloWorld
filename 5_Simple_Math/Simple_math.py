#-*- encoding: utf-8 -*-
from __future__ import print_function

number1 = int(input("What is the first number ? "))
number2 = int(input("What is the second number ? "))

print ("{n1} + {n2} = {ret1} \n{n1} - {n2} = {ret2} \n"
       "{n1} * {n2} = {ret3} \n{n1} \\ {n2} = {ret4} \n"
       .format(n1=number1, n2=number2, ret1=(number1 + number2), 
               ret2=(number1 - number2), ret3=(number1 * number2),
               ret4=(number1 / number2)))
