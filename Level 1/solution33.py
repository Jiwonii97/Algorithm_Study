# 코딩테스트 연습 / 연습문제 / 문자열 내 p와 y의 개수
# upper, lower 활용한 비교

def solution(s):
    s = s.lower()   # s.upper()
    return s.count("y") == s.count("p")