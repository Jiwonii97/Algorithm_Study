# https://www.acmicpc.net/problem/1916
# 최소비용 구하기
# 다익스트라 알고리즘(최단거리 알고리즘)를 응용한 탐색 문제

import sys
import heapq

MAX_DISTANCE = int(1e9)     # 최대거리

# 도시 수(N), 버스 수(M)
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
graph = [[] for _ in range(n + 1)]

# 간선 정보
for _ in range(m):
    x, y, cost = map(int, sys.stdin.readline().strip().split())
    graph[x].append((y, cost))

# 출발점과 도착점
start, end = map(int, sys.stdin.readline().strip().split())

# 다익스트라 알고리즘
def dijkstra(start):
    distances = [MAX_DISTANCE] * (n + 1)
    distances[start] = 0
    pq = [(0, start)]  # (비용, 노드) : 비용을 기준으로 정렬
    
    while pq:
        current_cost, current_node = heapq.heappop(pq)
        
        # 이전에 구한 거리가 더 최소 거리인 경우, 생략
        if current_cost > distances[current_node]:
            continue
        
        # 인접 노드 탐색
        for next_node, next_cost in graph[current_node]:
            total_cost = current_cost + next_cost
            
            # 최단 거리인 경우
            if total_cost < distances[next_node]:
                distances[next_node] = total_cost       # 업데이트
                heapq.heappush(pq, (total_cost, next_node))
    
    return distances

distances = dijkstra(start)
print(distances[end])