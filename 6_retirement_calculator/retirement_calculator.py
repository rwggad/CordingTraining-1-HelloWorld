# -*- encoding: utf-8 -*-
from __future__ import print_function
from datetime import datetime 
from dateutil.relativedelta import relativedelta

user_age = int(raw_input("What is your age ? "))
user_retire_age = int(raw_input("At what age would you like to retire ? "))
user_remind_age = (user_retire_age - user_age)

if user_remind_age < 0:
    print("you alreay retire!")
    quit()

now_date = datetime.now()
retire_date = (now_date + relativedelta(years=user_retire_age))

print ("You have {} years left until you can retire.".format(user_retire_age))
print ("It's {}, so you can retire in {}".format(now_date.year, retire_date.year))
