# www.acmicpc.net/problem/11050
# 이항계수1
# 팩토리얼 함수 직접 구현을 통한 수학 문제
# O(N)

import sys

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

n, k = map(int, sys.stdin.readline().strip().split())
n1 = factorial(n)
n2 = factorial(k)*factorial(n-k)
print(n1//n2)

