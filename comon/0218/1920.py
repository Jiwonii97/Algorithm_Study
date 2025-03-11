# https://www.acmicpc.net/problem/1920
# 수 찾기
# set을 활용한 단순 문제

'''
    예시 : 
        5
        4 1 5 2 3
        5
        1 3 7 9 5

        1
        1
        0
        0
        1
'''

import sys

n_count = int(sys.stdin.readline().strip())     # 입력
n_number = list(map(int, sys.stdin.readline().strip().split(' ')))

number_queue = set()

for n in n_number:
    number_queue.add(n)


m_count = int(sys.stdin.readline().strip())     # 입력
m_number = list(map(int, sys.stdin.readline().strip().split(' ')))

for m in m_number:
    print(int(m in number_queue))
