# 코딩테스트 연습 / 힙(Heap) / 더 맵게

def solution(scoville, K):
    import heapq
    answer = 0
    heapq.heapify(scoville)    
    
    while len(scoville) >= 2:
        n1 = heapq.heappop(scoville)
        # 만약 제일 적은 수가 해당 스코빌을 넘길 경우, 반복문 종료
        if n1 >= K:
            break
        
        # 아닐 경우, 새로운 스코빌 데이터를 추가
        n2 = heapq.heappop(scoville)
        heapq.heappush(scoville,n1+n2*2)
        
        answer += 1
    
    return answer if scoville[0] >= K else -1

print(solution([1, 2, 3, 9, 10, 12],7))