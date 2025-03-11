# https://www.acmicpc.net/problem/6064
# 카잉 달력
# 단순 스택 구현 문제, 입력과 함께 구하는 것이 시간단축의 포인트

import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().strip().split())

    result = -1
    for num in range(x, (m*n)+1, m):
        if ((num-x)%m == 0) and ((num-y)%n == 0):
            result = num
            break

    print(result)