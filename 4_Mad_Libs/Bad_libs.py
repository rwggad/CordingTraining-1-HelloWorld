# -*- encoding: utf-8 -*-
from __future__ import print_function

# 명사 동사 형용사 부사 입력
input_noun = raw_input('Enter a noun: ')
input_verb = raw_input('Enter a verb: ')
input_adjective = raw_input('Enter a adjective: ')
input_adverb = raw_input('Enter a adverb: ')

# 엉뚱한 이야기 구성
my_story = "do you "+ input_verb + " your " + input_adjective + " " + \
        input_noun + " " + input_adverb + "? That's hilarious!"

# 이야기 출력 
print (my_story)
