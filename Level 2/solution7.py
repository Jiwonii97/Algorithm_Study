# 코딩테스트 연습 / 스택/큐 / 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    answer = 0
    sum_bridge = 0
    bridge = []
    bridge_time = []
    
    # truck_weights : 남은 트럭 / bridge : 현재 트럭
    while truck_weights or bridge:
        
        # 다리가 비어있으면 그냥 올림
        if len(bridge) == 0:
            temp = truck_weights.pop(0)
            bridge.append(temp)
            bridge_time.append(answer)
            sum_bridge += temp
            answer += 1
            continue

        # 제일 앞에 있는 트럭이 나가는지 확인
        if answer - bridge_time[0] == bridge_length:
            sum_bridge -= bridge[0]
            del bridge[0]
            del bridge_time[0]
            
        # 현재 다리에 더 트럭이 올라갈 수 있는지 확인해서 올림
        if truck_weights and sum_bridge + truck_weights[0] <= weight:
            temp = truck_weights.pop(0)
            bridge.append(temp)
            bridge_time.append(answer)
            sum_bridge += temp
        
        answer +=1
        
    return answer

print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))

'''
    < 다른 풀이 >
    # collection, deque 사용
    # 시간을 따로 계산하지 않고 popleft()와 직접 0과 함께 숫자를 넣어 시간 계산 진행
    from collections import deque

    def solution(bridge_length, weight, truck_weights):
        bridge = deque(0 for _ in range(bridge_length)) # 다리의 위치 정보라고 이해
        total_weight = 0    # 전체 다리 위에있는 트럭의 무게
        step = 0        # 단계 수
        truck_weights.reverse()     # 왜 reverse를 할까?? : -1 인덱스에 대한 걱정이 없음 / 차피 Queue 형식으로 빼는건 똑같으니깐

        while truck_weights:
            total_weight -= bridge.popleft()
            if total_weight + truck_weights[-1] > weight:
                bridge.append(0)
            else:
                truck = truck_weights.pop()
                bridge.append(truck)
                total_weight += truck
            step += 1

        step += bridge_length

        return step
'''