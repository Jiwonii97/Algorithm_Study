# 코딩테스트 연습 / 탐욕법(Greedy) / 체육복

def solution(n, lost, reserve):
    answer = 0
    _dict = {x:1 for x in range(1,n+1)}
    for id in lost:
        _dict[id]-=1
    for id in reserve:
        _dict[id]+=1
        
    for sid in range(1,n+1):
        if sid in _dict.keys() and _dict[sid] == 0:
            if sid-1 >= 1 and _dict[sid-1] == 2:
                _dict[sid-1] -= 1
                _dict[sid] += 1
            elif sid+1 <= n and _dict[sid+1] == 2:
                _dict[sid+1] -= 1
                _dict[sid] += 1
            else:
                continue
        
    for value in _dict.values():
        if value >=1:
            answer+=1
            
    return answer


print(solution(5,[2, 4],[1, 3, 5]))
print(solution(5,[2, 4],[3]))
print(solution(3,[3],[1]))

'''
< 다른 풀이 >
def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n+1):
        if i not in lost: #안 잃어버린 학생
            answer += 1
        else:
            if i in reserve: #잃어버렸지만 여분도 있는 학생
                answer += 1
                reserve.remove(i)
                lost.remove(i)

    for i in lost: #잃어버리고 여분도 없어서 빌려야 하는 학생
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)
        elif i+1 in reserve:
            answer +=1
            reserve.remove(i+1)

    return answer
'''