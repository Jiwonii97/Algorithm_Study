# https://school.programmers.co.kr/learn/courses/30/lessons/132266?language=python3
# 부대복귀
# 조금 복잡한 BFS 그래프 문제, 방문했던 기록만을 사용하면 시간초과가 날 수 있어 계산할 때마다 중간 지점을 계속 업데이트를 하면서 다음 계산에 활용

from collections import deque
def solution(n, roads, sources, destination):
    answer = []

    graph = [[] for _ in range(n + 1)]
    for n1, n2 in roads :
        graph[n1].append(n2)
        graph[n2].append(n1)

    costs = [-1 for _ in range(n + 1)]
    costs[destination] = 0

    queue = deque([destination])
    while queue :
        x = queue.popleft()
        for node in graph[x] :
            if costs[node] == -1 :
                queue.append(node) 
                costs[node] = costs[x] + 1

    for s in sources :
        answer.append(costs[s])

    return answer

print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))