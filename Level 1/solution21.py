# 코딩테스트 연습 / 월간 코드 챌린지 시즌1 / 두 개 뽑아서 더하기
# sorted 하는거 놓치지 않아야 할듯 (정석풀이) _ 출력값에 따라 정렬유무 판단
 
def solution(numbers):
    length = len(numbers)
    answer = []
    
    for i in range(length):
        for j in range(i+1,length):
            answer.append(numbers[i]+numbers[j])
            
    answer = sorted(list(set(answer)))
    
    return answer