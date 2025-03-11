# https://www.acmicpc.net/problem/1260
# DFS와 BFS
# 단순 dfs, bfs 구현 문제

import sys
from collections import defaultdict

n, m, v = map(int, sys.stdin.readline().strip().split())
lines = defaultdict(list)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    lines[a].append(b)
    lines[b].append(a)

def dfs(v, lines, visited):
    visited[v] = True
    output = [v]
    
    for i in sorted(lines[v]):
        if not visited[i]:
            output.extend(dfs(i, lines, visited))
            
    return output
    

def bfs(v, lines):
    dq = [v]
    output = []
    while dq:
        point = dq.pop(0)
        if point in output:
            continue
        output.append(point)
        dq.extend(sorted(lines[point]))
        
    return output

# dfs
visited = [False]*(n+1)
print(' '.join(map(str, dfs(v, lines, visited))))

# bfs
print(' '.join(map(str, bfs(v, lines))))