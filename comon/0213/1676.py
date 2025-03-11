# https://www.acmicpc.net/problem/1676
# 팩토리얼 0의 개수
# 문자열 역순 + 순차적 검색

'''
    예시 : 
        1)    10  2
        2)    3   0
'''

import sys
text = sys.stdin.readline().strip()     # 입력

point = 1
for i in range(1, int(text)+1):
    point *= i

point = str(point)[::-1]            # 타겟 숫자 역순

output = 0
for c in point:     # 0의 개수 확인
    if c != '0':
        break
    output += 1

print(output)       # 출력
