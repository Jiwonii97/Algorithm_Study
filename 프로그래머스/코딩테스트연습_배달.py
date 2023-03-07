# https://school.programmers.co.kr/learn/courses/30/lessons/12978

def solution(N, road, K):
    import heapq

    graph = [[] for _ in range(N+1)]
    dist = [float("inf")]*(N+1)

    for s, e, c in road:
        graph[s].append([e, c])
        graph[e].append([s, c])

    def dijkstra(graph, dist):
        hq = []
        heapq.heappush(hq, [1, 0])
        dist[1] = 0

        while hq:
            point, cost = heapq.heappop(hq)
            if dist[point] > cost:
                continue

            for npoint, ncost in graph[point]:
                cst = cost + ncost      # 이 길을 거쳐가면 거리가 얼마나 될까?
                # 우리가 새로운 길을 뚫고 왔는데 여기가 최소 거리니?
                if dist[npoint] > cst:
                    dist[npoint] = cst
                    heapq.heappush(hq, [npoint, cst])   # 맞으면 이걸로 업데이트를 다시 해보자

    dijkstra(graph, dist)

    return len([x for x in dist[1:] if x <= K])


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2],
      [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
# print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [
#       3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))
