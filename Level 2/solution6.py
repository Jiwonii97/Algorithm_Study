# 코딩테스트 연습 / 스택/큐 / 기능개발

def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0
        progresses = [x+y for x,y in zip(progresses, speeds)]
        
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
            
        if cnt != 0 :
            answer.append(cnt)
            
    return answer

print(solution([93, 30, 55],[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))