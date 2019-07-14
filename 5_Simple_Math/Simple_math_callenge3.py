#-*- encoding: utf-8 -*-
from __future__ import print_function

class InvalidInputValue(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


def my_input():
    input_value = raw_input("What is the number ? ")
    if input_value.isdigit() == False: # input value is number ?
        raise InvalidInputValue('Input Value is only number ({})'
                .format(input_value))
    if int(input_value) < 0: # input number is positive number ?
        raise InvalidInputValue("Input number is only positive number ({})"
                .format(input_value))
    return int(input_value)


try:
    number1 = my_input()
    number2 = my_input()
    print ("{n1} + {n2} = {ret1} \n{n1} - {n2} = {ret2} \n"
           "{n1} * {n2} = {ret3} \n{n1} \\ {n2} = {ret4} \n"
           .format(n1=number1, n2=number2, ret1=(number1 + number2), 
                   ret2=(number1 - number2), ret3=(number1 * number2),
                   ret4=(number1 / number2)))
except InvalidInputValue as e:
    print(e)
