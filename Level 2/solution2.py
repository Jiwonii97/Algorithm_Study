# 코딩테스트 연습 / 연습문제 / 최솟값 만들기
# zip 활용 문제

def solution(A,B):
    A = sorted(A)
    B = sorted(B,reverse=True)
    return sum([x*y for x,y in zip(A,B)])