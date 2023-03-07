# https://school.programmers.co.kr/learn/courses/30/lessons/12978

def solution(n, s, a, b, fares):
    maxNum = float("inf")
    dist = [[maxNum] * (n + 1) for _ in range(n + 1)]
    for i, j, cost in fares:
        dist[i][j] = dist[j][i] = cost

    for i in range(1, n + 1):  # 자기 자신 0으로 초기화
        dist[i][i] = 0

    for k in range(1, n + 1):       # dp를 응용하여 중간 연결 확인
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    answer = maxNum
    for i in range(1, n + 1):
        # S에서 출발해서 각 노드를 거쳐 A,B까지 얼마나 나오는지 계산, 가장 적게 나오는 요금을 답으로 채택
        # [S -> i 요금 + i -> A 요금 + i -> B 요금]
        cost = dist[s][i] + dist[i][a] + dist[i][b]
        answer = min(answer, cost)
    return answer


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [
      5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4],
      [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [
      6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))

'''
    플로이드-워셜 알고리즘을 이용하여 푸는 문제
    문제의 요구 사항은 S에서 출발하여 특정 노드까지 택시를 타고 이동하고(S -> i), 특정 노드에서 다시 A와 B로 흩어지는 것이기 때문에(i -> A, i -> B) 모든 노드간 최단 거리 값을 구해야 합니다.
    모든 노드끼리의 최단 거리 값을 플로이드 워셜 알고리즘을 이용해 구해준 뒤 다음의 값 중 가장 작은 값을 답으로 채택합니다.
    
    S -> 1번 노드 최단 거리 + 1번 노드 -> A + 1번 노드 -> B
    S -> N번 노드 최단 거리 + N번 노드 -> A + N번 노드 -> B
    
    처음 inf의 값을 정할 땐 최대 요금인 100,000과 모든 노드의 개수인 200을 곱한 20,000,000 보다 높은 값으로 정해주면 됩니다.
'''
