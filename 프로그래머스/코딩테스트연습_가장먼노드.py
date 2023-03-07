# https://school.programmers.co.kr/learn/courses/30/lessons/49189
'''
    그래프 문제 -> BFS로 해결

'''

from collections import deque


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]  # 연결된 노드 정보 그래프
    distance = [-1] * (n+1)  # 각 노드의 최단거리 리스트

    # 연결된 노드 정보 추가
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    queue = deque([1])  # BFS를 위한 큐, 출발 노드는 1
    distance[1] = 0  # 출발 노드의 최단거리 0으로
    # BFS 수행
    while queue:
        now = queue.popleft()  # 현재 노드

        # 현재 노드에서 이동할 수 있는 모든 노드 확인
        for i in graph[now]:
            if distance[i] == -1:  # 아직 방문하지 않은 노드라면
                queue.append(i)  # 큐에 추가
                distance[i] = distance[now] + 1  # 최단거리 갱신

    # 가장 멀리 떨어진 노드 개수 구하기
    for d in distance:
        if d == max(distance):
            answer += 1

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))


'''
    # BFS 사용했지만 시간초과 발생
    def solution(n, edge):
        from collections import defaultdict
        answer = []
        myEdges = defaultdict(list)

        for e in edge:
            n1, n2 = e
            myEdges[n1].append(n2)
            myEdges[n2].append(n1)

        for num in range(2, n+1):
            if 1 in myEdges[num]:
                answer.append([num, 1])
                continue
            elif not myEdges[num]:
                answer.append([num, 0])
                continue

            bfs = [[x, 1] for x in myEdges[num]]
            while True:
                point, length = bfs.pop(0)

                if 1 in myEdges[point]:
                    answer.append([num, length+1])
                    break
                else:
                    if myEdges[point]:
                        bfs.extend([x, length+1] for x in myEdges[point])

        answer.sort(key=lambda x: x[1])

        maxNum, cnt = 0, 0
        for a in answer:
            if a[1] > maxNum:
                maxNum = a[1]
                cnt = 1
            elif a[1] == maxNum:
                cnt += 1

        return cnt
'''
