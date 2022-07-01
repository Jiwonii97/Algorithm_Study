# 코딩테스트 연습 / 연습문제 / 문자열 내림차순으로 배치하기
# join 활용 방법

def solution(s):
    return "".join(sorted(list(s),reverse=True))