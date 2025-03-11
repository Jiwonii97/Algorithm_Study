# https://www.acmicpc.net/problem/2609
# 최대공약수와 최소공배수
# 유클리드 호제법과  lcm*gcd = a*b 을 이용한 풀이 방법 O(logN)

import sys

a, b = map(int, sys.stdin.readline().strip().split())

# 유클리드 호제법을 활용한 최대공약수
def gcd(n, m):
    while m > 0:
        n, m = m, n % m
    return n

def lcm(n, m):
    return (n*m)//gcd(n, m)

print(gcd(a, b))
print(lcm(a, b))