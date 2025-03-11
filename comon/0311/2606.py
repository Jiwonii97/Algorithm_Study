# https://www.acmicpc.net/problem/2606
# 바이러스
# visited를 응용한 BFS 문제 (O(V + E))

import sys
from collections import defaultdict

n = int(sys.stdin.readline().strip())
v = int(sys.stdin.readline().strip())

lines = defaultdict(list)

for _ in range(v):
    s, e = map(int, sys.stdin.readline().strip().split())
    lines[s].append(e)
    lines[e].append(s)
    
visited = [False]*(v+100)
dq = [1]
visited[1] = True

while dq:
    for l in lines[dq.pop(0)]:
        if not visited[l]:
            dq.append(l)
            visited[l] = True

print(visited.count(True)-1)
    
    
    
    
