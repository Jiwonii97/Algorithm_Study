# https://www.acmicpc.net/problem/11651
# 좌표 정렬하기 2
# 정렬, lambda를 응용한 sort 진행

import sys
input = sys.stdin.readline

n = int(input().strip())
dq = []
for _ in range(n):
    x, y = map(int, input().strip().split())
    dq.append((x, y))
dq.sort(key=lambda x: (x[1], x[0]))

for d in dq:
    print(f"{d[0]} {d[1]}")
