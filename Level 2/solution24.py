# 코딩테스트 연습 / 완전탐색 / 전력망을 둘로 나누기
# wires 최대 길이가 100-1 밖에 되지 않으므로, 리스트를 순회하며 모든 경우의 수를 계산
# 트리형이기 때문에 그래프 간에 사이클이 존재하지 않음
# deque 형태로 사이클을 돌리며 모든 전력망을 두 그룹으로 나눌때까지 반복문을 진행

def solution(n, wires):
    answer = n
    
    for num in range(len(wires)):
        task1 = set([wires[num][0]])
        task2 = set([wires[num][1]])
        
        tasks = wires[:num] + wires[num+1:]
        
        while tasks:
            task = tasks.pop(0)
            
            # 첫번째 타워가 첫번째 그룹에 있는지 확인
            if task[0] in task1:
                task1.add(task[1])
                
            # 첫번째 타워가 두번째 그룹에 있는지 확인
            elif task[0] in task2:
                task2.add(task[1])    
                                
            # 두번째 타워가 첫번째 그룹에 있는지 확인
            elif task[1] in task1:
                task1.add(task[0])
                
            # 두번째 타워가 두번째 그룹에 있는지 확인
            elif task[1] in task2:
                task2.add(task[0])
                
            # 다 없는 경우 일단 다시 집어 넣음
            else:
                tasks.append(task)
                    
        diff = abs(len(task1) - len(task2))
        
        if diff < answer:
            answer = diff
        
    return answer

print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4,[[1,2],[2,3],[3,4]]))
print(solution(7,[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))

'''
    < 다른 풀이 >
    # set을 통해 중복을 제거하면서 두 set 사이에 & 연산을 통해 하나라도 중복된 값이 있는지 확인하고 조건에 맞는 경우 update를 통해 set에 계속 추가해 나감
    def solution(n, wires):
        ans = n
        for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):
            s = set(sub[0])
            [s.update(v) for _ in sub for v in sub if set(v) & s]
            ans = min(ans, abs(2 * len(s) - n))
        return ans
'''