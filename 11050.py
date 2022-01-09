"""

11050 - 이항 계수1

자연수(N)과 정수(K)가 주어졌을 때 이항 계수(N/K)를 구하는 프로그램을 작성하시오.

"""


def factorial(num):
    if num == 1 or num == 0:
        return 1
    return num * factorial(num-1)


binomial = input().split()
N = int(binomial[0])
K = int(binomial[1])

print(int(factorial(N)/(factorial(K)*factorial(N-K))))
