# www.acmicpc.net/problem/1012
# 유기농 배추
#
#

import sys
t = int(sys.stdin.readline().strip())

movement = [(0, -1), (1, 0), (0, 1), (-1, 0)]
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().strip().split())
    mat = [[0]*m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().strip().split())
        mat[y][x] = 1
    
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            # 이전에 방문한 적이 있으면 패스
            if visited[i][j]:
                continue
            
            if mat[i][j] == 1:
                dq = [(i, j)]
                while dq:
                    px, py = dq.pop(0)
                    
                    for dx, dy in movement:
                        if px+dxll
                        if mat[px+dx]
            
            visited[i][j] = True