# 코딩테스트 연습 / 월간 코드 챌린지 시즌2 / 괄호 회전하기
# deque의 rotate와 stack을 사용해서 조건에 맞는 결과를 찾음

from collections import deque
def solution(s):
    answer = 0
    bracket = {'(':')', '[':']','{':'}'}
    
    dq = deque(s)
    
    for _ in range(len(s)):
        # stack을 사용하여 괄호 맞추기
        stacks = []
        for idx in range(len(s)):
            # 스택이 비어있으면 그냥 넣음
            if not stacks:
                stacks.append(dq[idx])
            # 스택이 결국 괄호를 완성 할 수 없는 경우 (여는 괄호가 안나옴)
            elif stacks[-1] not in bracket.keys():
                break
            # 여는 괄호와 닫는 괄호가 잘 나온 경우
            elif bracket[stacks[-1]] == dq[idx]:
                stacks.pop()
            # 일단 여는 괄호가 나온 경우
            else:
                stacks.append(dq[idx])
                
        # 스택이 비어있다면 answer += 1 
        if not stacks:
            answer += 1
            
        # 하나씩 이동
        dq.rotate(-1)
    
    return answer

print(solution("[](){}"))           # 3
print(solution("}]()[{"))           # 2
print(solution("[)(]"))           # 0
print(solution("}}}"))           # 0