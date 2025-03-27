# https://www.acmicpc.net/problem/10026
# 적록색약
# 그래프+BFS 문제, 현재값과 같은 주변 값을 찾아서 색약을 고려한 다른 value로 수정하여 다시 탐색 진행, 현재값 초기화를 고려하지 못한 점이 체크포인트
# O(N^2)

import sys

n = int(sys.stdin.readline().strip())
mat = [list(sys.stdin.readline().strip()) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 일반 케이스 확인
count = 0
for i in range(n):
    for j in range(n):
        # 이미 구한적 있는 케이스
        if mat[i][j] in [0, 1]:
            continue
        
        dq = [(i, j)]
        target = mat[i][j]      # 찾을 색상

        if target in ["R", "G"]:
            mat[i][j] = 0
        else:
            mat[i][j] = 1

        while dq:
            px, py = dq.pop(0)

            for idx in range(4):
                nx, ny = px+dx[idx], py+dy[idx]
                if (0<=nx<n and 0<=ny<n) and mat[nx][ny] == target:
                    dq.append((nx, ny))
                    
                    if target in ["R", "G"]:
                        mat[nx][ny] = 0
                    else:
                        mat[nx][ny] = 1

        count += 1

print(count, end=" ")

# 색약 케이스 확인
count = 0
for i in range(n):
    for j in range(n):
        # 이미 구한적 있는 케이스
        if mat[i][j] == -1:
            continue
        
        dq = [(i, j)]
        target = mat[i][j]      # 찾을 색상
        mat[i][j] = -1

        while dq:
            px, py = dq.pop(0)

            for idx in range(4):
                nx, ny = px+dx[idx], py+dy[idx]
                if (0<=nx<n and 0<=ny<n) and mat[nx][ny] == target:
                    dq.append((nx, ny))
                    mat[nx][ny] = -1

        count += 1

print(count)
