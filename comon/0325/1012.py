# www.acmicpc.net/problem/1012
# 유기농 배추
# 문제 예시와 실제 데이터가 조금 달라 헤맨 문제, BFS를 통해 풀이 가능
# O(m × n)

import sys
t = int(sys.stdin.readline().strip())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    dq = [(x, y)]
    mat[x][y] = 0

    while dq:
        px, py = dq.pop(0)

        for idx in range(4):
            nx, ny = px+dx[idx], py+dy[idx]

            if (0 <= nx < m and 0 <= ny < n) and mat[nx][ny] == 1:
                dq.append((nx, ny))
                mat[nx][ny] = 0


for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().strip().split())
    mat = [[0]*n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().strip().split())
        mat[x][y] = 1

    count = 0
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                bfs(i, j)
                count += 1

    print(count)
