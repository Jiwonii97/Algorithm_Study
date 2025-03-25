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
    count = 0
    for i in range(n):
        for j in range(m):
            print(f"> {i}, {j} / {mat[i][j]}")
            
            if mat[i][j] == 1:
                mat[i][j] == 0
                dq = [(i, j)]
                while dq:
                    print(">>> ",dq)
                    px, py = dq.pop(0)
                    mat[px][py] == 0

                    for dx, dy in movement:
                        # 행렬의 조건을 만족
                        if 0<=(px+dx)<n and 0<=(py+dy)<m:
                            if mat[px+dx][py+dy] == 1:
                                dq.append((px+dx,py+dy))
                            
                count += 1
            
            visited[i][j] = True
    print(count)