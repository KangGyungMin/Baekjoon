"""

1541 - 잃어버린 괄호

세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

"""
import re

expression = input()
sign = re.sub(r'[0-9]+', '', expression)
number = expression.replace('-', '+').split('+')
min = 0
switch = 0

for i in range(len(number)):
    if switch == 0:
        min += int(number[i])
    elif switch == 1:
        min -= int(number[i])

    if i != len(number)-1:
        if sign[i] == '-':
            if switch == 0:
                switch = 1

print(min)
