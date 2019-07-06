# -*- encoding: utf-8 -*-
from __future__ import print_function 

'''
@문제
    이름을 입력 받아서
    입력 받은 이름으로 인사말을 출력하는 프로그램 작성

@제약사항
    입력부분, 문자열 연결 부분, 출력 부분 별도로 작성 

'''

# 입력 부분
print ('Wate is your name? ', end='')
name = raw_input()

# 문자열 연결 부분
msg = 'Hello, ' + name + ', nice to meet you!'

# 출력 부분
print (msg);

