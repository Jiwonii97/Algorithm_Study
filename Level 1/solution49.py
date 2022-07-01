# 코딩테스트 연습 / 연습문제 / 콜라츠 추측
# 단순 수학 문제

def solution(num):
    answer = 0
    
    while(True):
        if num == 1:
            break
        if answer > 500:
            answer = -1
            break
        if num%2:
            num = int(num*3)+1
        else:
            num = int(num/2)
        answer += 1
            
    return answer

'''
    < 다른 풀이 >
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1
'''