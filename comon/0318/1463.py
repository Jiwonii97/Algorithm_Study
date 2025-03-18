# https://www.acmicpc.net/problem/1463
# 1로 만들기
# dp(동적 계획법), 1부터 목표값까지 순차적으로 조건에 맞는 경우에 대해 계산 진행, O(n)

import sys

n = int(sys.stdin.readline().strip())
a = [0]*(n+1)

for i in range(2, n+1):
    case = []
    if not i % 3:
        case.append(a[i//3]+1)
    if not i % 2:
        case.append(a[i//2]+1)
    case.append(a[i-1]+1)

    a[i] = min(case)

print(a[n])
