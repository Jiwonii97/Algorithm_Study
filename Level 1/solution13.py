# 코딩테스트 연습 / 완전탐색 / 모의고사

from math import ceil
def solution(answers):
    answer = []
    
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    student = [student1,student2,student3]
    length = len(answers)
    
    max = 0
    for s in range(3):
        cnt = ceil(length/len(student[s]))

        if cnt != 0:
            temp = student[s]*cnt
            temp = temp[:length]
        else:
            temp = student[s]
        
        score = 0
        for idx in range(length):
            if answers[idx] == temp[idx]:
                score += 1
        
        if max < score:
            answer = [s+1]
            max = score
        elif max == score:
            answer.append(s+1)
        else:
            continue
        
    return answer


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))


'''
< 다른 풀이 >
- enumerate로 인덱스와 해당 리스트 값을 한번에 가져올 수 있음
- 나머지 연산을 통해 반복적인 요소 제한 (곱하는 거 보다 쉬운 방법)
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
'''