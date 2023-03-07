# https://school.programmers.co.kr/learn/courses/30/lessons/12979

'''
    이중 포인터 사용, BFS/DFS 아님
'''

import math


def solution(n, stations, w):
    W = w * 2 + 1
    count, start = 0, 1
    for s in stations:
        end = s - w     # 반대에서 부터 이동
        if end < 2:     # 처음부터 기지국이 잘 자리를 잡은 경우, 시작 위치를 재조정
            start = s + w + 1
        else:
            house = end-start
            count += math.ceil(house/W)
            start = s + w + 1       # 다음 시작 포인트 지정

    if s + w < n:       # 아직 전파가 필요한 경우
        start = s + w
        house = n - start
        count += math.ceil(house/W)

    return count


print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))
