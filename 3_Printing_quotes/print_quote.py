# -*- encoding: utf-8 -*-
from __future__ import print_function

# 인용구 입력
print ('What is the quote ? ', end='')
input_quote = raw_input()

# 인용구를 한 사람 이름 입력
print ('Who said it ? ', end='')
input_said_people = raw_input()

# 따옴표를 활용하여 사람 + 인용구 출력
print( input_said_people + ' says, ' + '\"' + input_quote + '.\"')
