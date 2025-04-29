# https://www.acmicpc.net/problem/1929
# 소수 구하기
# 수학/소수, 에라토스테네스의 체 응용 문제
# O(NlogN)

import sys
input = sys.stdin.readline

m, n = map(int, input().strip().split())
is_prime = [False, False] + [True]*n

for i in range(2, n+1):
    if is_prime[i]:
        for j in range(2*i, n+1, i):
            is_prime[j] = False

for idx, ip in enumerate(is_prime[m:n+1], start=m):
    if ip:
        print(idx)