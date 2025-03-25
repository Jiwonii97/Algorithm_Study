# https://www.acmicpc.net/problem/2018
# 수들의 합 5
# 투 포인터 문제, 포인터를 움직여가며 해당 범위까지의 계산을 진행, 중간을 넘어가면 두 수의 합이 오버가 되기 때문에 중간까지만 계산 진행
# O(n)

import sys

n = int(sys.stdin.readline().strip())

px, py = 1, 1
target, count = 1, 1

# 중간까지만 확인하면 됨
while px < n//2+1:
    if target == n:
        count += 1
        py += 1
        target += py
    elif target > n:
        target -= px
        px += 1
    else:
        py += 1
        target += py

print(count)
