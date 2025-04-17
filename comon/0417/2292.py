# https://www.acmicpc.net/problem/2292
# 벌집

import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(1)
else:
    idx = 1
    n -= 1

    while n > 0:
        n -= idx*6
        idx += 1

    print(idx)
