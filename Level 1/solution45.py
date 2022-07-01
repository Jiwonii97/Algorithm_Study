# 코딩테스트 연습 / 연습문제 / 정수 제곱근 판별
# sqrt : 제곱근, pow : 제곱수

from math import sqrt
def solution(n):

    if  int(sqrt(n)) == sqrt(n):
        return pow(sqrt(n) + 1, 2)
    else:
        return -1