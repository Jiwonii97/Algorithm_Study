# https://www.acmicpc.net/problem/1697
# 숨바꼭질
# BFS/DFS, BFS 적용한 문제
# BFS에 꼭 visited 적용, 다음 삽입 데이터 조건식 잘 세우기

import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().strip().split())
MAXLEN = 100001

dq = deque([(n, 0)])
visited = [False]*MAXLEN
while dq:
    point, count = dq.popleft()
    visited[point] = True
    
    # 동생 위치에 도착
    if point==k:
        print(count)
        break
    
    for new_point in [point+1, point-1, point*2]:
        if 0<=new_point<MAXLEN and not visited[new_point]:
            dq.append((new_point, count+1))