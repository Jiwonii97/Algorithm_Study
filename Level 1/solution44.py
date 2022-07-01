# 코딩테스트 연습 / 연습문제 / 정수 내림차순으로 배치하기
# 정렬 후 reverse 시켜 이어붙임

def solution(n):
    return int("".join(sorted(list(str(n)),reverse = True)))