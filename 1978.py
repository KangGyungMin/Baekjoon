"""

1978 - 소수 찾기

주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

"""


def detect_prime(num, count=None):
    if num == 1:
        return 0
    if count == None:
        count = num - 1
    if count == 1:
        return 1
    elif num % count == 0:
        return 0

    return detect_prime(num, count-1)


N = int(input())
N2 = input().split()
N2 = list(map(int, N2))
sum = 0

for i in N2:
    if detect_prime(i) == 1:
        sum += 1

print(sum)
