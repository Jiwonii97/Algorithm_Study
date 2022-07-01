# 코딩테스트 연습 / 연습문제 / 최댓값과 최솟값

def solution(s):
    list_ = sorted(map(int,s.split()))
    return "{} {}".format(list_[0],list_[-1])