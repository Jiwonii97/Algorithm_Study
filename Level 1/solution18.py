# 코딩테스트 연습 / 월간 코드 챌린지 시즌2 / 약수의 개수와 덧셈

import math
def solution(left, right):
    answer = 0
    
    for num in range(left,right+1):
        cal=[]
        for n1 in range(1,int(num)+1):
            if num % n1 == 0:
                cal.append(n1)
                cal.append(int(num/n1))
                
        cal = set(cal)
        answer += num*pow((-1),len(cal))
    
    return answer

'''
< 다른 풀이 >
# 제곱수인 경우 약수의 개수가 홀수 인것을 활용한 제곱수를 이용한 방식
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
'''