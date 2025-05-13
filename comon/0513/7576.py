# https://www.acmicpc.net/problem/7576
# 토마토
# BFS, 큐에 1에 대한 데이터를 확장시키고 이에 BFS를 통해 전체 탐색 진행
# O(N^2)

import sys
from collections import deque
input = sys.stdin.readline

dy = [0, 0, -1 ,1]
dx = [-1, 1, 0, 0]

m, n = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

dq = deque()
for i in range(n):
    for j in range(m):
        if mat[i][j] == 1:
            dq.append((i, j, 0))

max_count = 0
while dq:
    x, y, count = dq.popleft()
    max_count = max(max_count, count)

    for idx in range(4):
        nx, ny = x+dx[idx], y+dy[idx]
        if ((0<=nx<n)and(0<=ny<m)) and mat[nx][ny] == 0:
            dq.append((nx, ny, count+1))
            mat[nx][ny] = 1

non_flag = False
for i in range(n):
    for j in range(m):
        if mat[i][j] == 0:
            non_flag = True

print(-1 if non_flag else max_count)