# 코딩테스트 연습 / 탐욕법(Greedy) / 섬 연결하기
# 크루스칼 알고리즘 활용 : 정렬 후, 가치가 낮은 간선부터 선택하여 각 지점을 연결 ( 그리디 )

def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2]) 
    link = set([costs[0][0]])       # 이미 연결된 정점들

    # Kruskal 알고리즘으로 최소 비용 구하기
    while len(link) != n:
        for cost in costs:
            
            # 이미 작업한 경우
            if cost[0] in link and cost[1] in link:
                continue
            
            # 새로 연결할 경우
            if cost[0] in link or cost[1] in link:
                link.update([cost[0], cost[1]])     # update : 해당 리스트의 값을 set에 추가(다수의 append 처리)
                answer += cost[2]
                break
                
    return answer

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))    # 4
print(solution(5,[[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]))    # 15
print(solution(5,[[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]])) # 8
print(solution(4,[[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]]))  # 9
print(solution(5,[[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]]))    # 104
print(solution(6,[[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]))    # 11
print(solution(5,[[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]]))    # 6
print(solution(5,[[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]]))  # 8
print(solution(5,[[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]]))  # 8