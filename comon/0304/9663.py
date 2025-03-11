# https://www.acmicpc.net/problem/10845
# 미로 탐색

import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, sys.stdin.readline().strip().split())
maze = [list(map(int, str(input().strip()))) for _ in range(n)]  # 지도 정보 입력
visited = [[False]*m for _ in range(n)]

dq = deque([(0, 0)])
visited[0][0] = True

while dq:
    x, y = dq.popleft()

    # 목표 도달
    if x == n-1 and y == m-1:
        break

    # 다음 이동 진행
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        # 갈 수 없는 곳이거나 이미 방문한 경우
        if not (0 <= nx < n and 0 <= ny < m):
            continue
        if (maze[nx][ny] == 1) and (not visited[nx][ny]):
            dq.append((nx, ny))
            maze[nx][ny] += maze[x][y]

print(maze[n-1][m-1])
