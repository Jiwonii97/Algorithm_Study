# 코딩테스트 연습 / 연습문제 / 문자열 내 마음대로 정렬하기
# key값으로 lambda 함수를 활용해 원하는 방식으로 정렬시킴

def solution(strings, n):
    return sorted(strings, key = lambda x: (x[n],x))