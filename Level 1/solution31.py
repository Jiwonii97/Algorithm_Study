# 코딩테스트 연습 / 연습문제 / 두 정수 사이의 합
# range, sum 활용

def solution(a, b):
    return sum(range(min(a,b),max(a,b)+1))