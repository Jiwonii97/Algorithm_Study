# https://www.acmicpc.net/problem/1026
# 보물

import sys

_input = int(sys.stdin.readline())
numA = sorted(map(int, sys.stdin.readline().split()))
numB = sorted(map(int, sys.stdin.readline().split()))

res = sum([x*y for x, y in zip(numA[::-1], numB)])
print(res)
