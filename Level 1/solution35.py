# 코딩테스트 연습 / 연습문제 / 문자열 다루기 기본
# isdigit() 활용

def solution(s):
    return s.isdigit() if (len(s) == 4 or len(s) == 6) else False

'''
    < 다른 풀이 >
    return s.isdigit() and len(s) in (4, 6)
'''