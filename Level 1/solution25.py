# 코딩테스트 연습 / 위클리 챌린지 / 부족한 금액 계산하기
# max, sum을 활용한 수학 구현문제

def solution(price, money, count):
    return max(0,sum(list(price*x for x in range(1,count+1))) - money)