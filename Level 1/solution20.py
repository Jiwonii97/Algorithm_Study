# 코딩테스트 연습 / Summer/Winter Coding(~2018) / 예산
# 유사 knapsack 문제 _ 정렬후 낮은 값을 빼어 많은 양이 남도록 함

def solution(d, budget):
    answer = 0
    d.sort()
    
    for prize in d:
        budget -= prize
        if budget >= 0:
            answer += 1
        else:
            break
    
    return answer