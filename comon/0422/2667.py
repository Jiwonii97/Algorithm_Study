# https://www.acmicpc.net/problem/2667
# 단지번호붙이기
# BFS, 중복된 apt를 확인하지 않도록 queue 체크, 그 외에는 이전같이 BFS로 문제 풀이 진행
# O(n^2)

import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input().strip())
mat = [list(input().strip()) for _ in range(n)]

count = 0
apt = []
for i in range(n):
    for j in range(n):
        if mat[i][j] == '1':
            dq = deque([(i, j)])
            apt_count = 0
            
            while dq:
                x, y = dq.popleft()  # O(1) 시간
                mat[x][y] = '0'
                apt_count += 1
                for idx in range(4):
                    if (0 <= x+dx[idx] < n and 0 <= y+dy[idx] < n) and mat[x+dx[idx]][y+dy[idx]] == '1':
                        if (x+dx[idx], y+dy[idx]) not in dq:
                            dq.append((x+dx[idx], y+dy[idx]))
            
            apt.append(apt_count)
            count += 1

print(count)
for a in sorted(apt):
    print(a)