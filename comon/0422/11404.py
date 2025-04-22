# https://www.acmicpc.net/problem/11404
# 플로이드
# DP+플로이드-워셜 알고리즘 적용, 알고리즘 공부 필요

import sys
MAXLEN = int(1e5)
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

distance = [[MAXLEN]*n for _ in range(n)]

for i in range(n):
    distance[i][i] = 0
    
for _ in range(m):
    s, e, d = map(int, input().strip().split())
    distance[s-1][e-1] = min(distance[s-1][e-1],d)

for k in range(n):
    for i in range(n):
        for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])

for i in range(n):
    for j in range(n):
        if distance[i][j] == MAXLEN:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()