# https://www.acmicpc.net/problem/1753
# 최단경로
# 서로 다른 가중치를 가진 그래프의 최단거리 문제는 '다익스트라 알고리즘'을 적용

import sys
import heapq

INF = int(1e9)

v, e = map(int, sys.stdin.readline().strip().split())
start = int(sys.stdin.readline().strip())
mat = [[] for _ in range(v+1)]

for _ in range(e):
    m, n, d = map(int, sys.stdin.readline().strip().split())
    mat[m].append((n, d))

def dijkstra(start, n, graph):
    distances = [INF]*(n+1)
    distances[start] = 0
    
    dq = [(0, start)]
    
    while dq:
        cost, node = heapq.heappop(dq)
        
        if cost > distances[node]:
            continue
        
        for next_node, next_cost in graph[node]:
            total_cost = next_cost + cost
            
            if total_cost < distances[next_node]:
                distances[next_node] = total_cost
                heapq.heappush(dq, (total_cost, next_node))
                
    return distances

distances = dijkstra(start, v, mat)
for distance in distances[1:]:
    if distance == INF:
        print("INF")
    else:
        print(distance)