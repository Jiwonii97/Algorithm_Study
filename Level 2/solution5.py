# 코딩테스트 연습 / 스택/큐 / 프린터
# queue와 deque 활용

def solution(priorities, location):
    if len(priorities) == 1:
        return 1
    
    length_ = len(priorities)
    cnt = 1
    temp = priorities.pop(0)
    
    while priorities:
        if location > 0:
            if temp >= max(priorities):
                cnt+=1
            else :
                priorities.append(temp)
            location -= 1
        else:
            if temp >= max(priorities):
                break
            else :
                priorities.append(temp)
                location = len(priorities)-1
        temp = priorities.pop(0)
    
    if priorities:
        return cnt
    else :
        return length_
    
'''
    < 다른 풀이 >
    def solution(priorities, location):
        queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

    def solution(priorities, location):
        jobs = len(priorities)
        answer = 0
        cursor = 0
        while True:
            if max(priorities) == priorities[cursor%jobs]:
                priorities[cursor%jobs] = 0
                answer += 1
                if cursor%jobs == location:
                    break
            cursor += 1   
        return answer
'''