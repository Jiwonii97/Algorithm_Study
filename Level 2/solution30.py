# 코딩테스트 연습 / 탐욕법(Greedy) / 단속카메라
# 이전 solution29 응용, 인덱스를 넘어가면서 이전꺼와 비교하며 조건에 맞는 값을 도출

def solution(routes):
    routes.sort()
    answer = 1
    
    [cstart, cend] = routes[0]
    for idx in range(1,len(routes)):
        [start, end] = routes[idx]
        
        # 범위 밖
        if cend < start:
            [cstart,cend] = routes[idx]
            answer += 1
            continue
        
        cstart = max(cstart, start)
        cend = min(cend, end)
    
    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))

'''
    < 다른 풀이 >
    def solution(routes):
        routes = sorted(routes, key=lambda x: x[1])
        last_camera = -30000

        answer = 0

        for route in routes:
            if last_camera < route[0]:
                answer += 1
                last_camera = route[1]

        return answer
'''