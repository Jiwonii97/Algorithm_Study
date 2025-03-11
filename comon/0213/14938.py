# https://www.acmicpc.net/problem/14938
# 서강그라운드
# 아직 안품

'''
    예시 : 
        5 5 4
        5 7 8 2 3
        1 4 5
        5 2 4
        3 2 3
        1 2 3

        23
'''

import sys
text = sys.stdin.readline().strip()     # 입력

cal_queue = []
sum_queue = []

# 수식 분리
current_target = ""
for c in text[::-1]:
    if str.isdigit(c):      # 숫자 분리
        current_target += c
    elif c == "+":      # 덧셈
        sum_queue.append(int(current_target[::-1]))
        current_target = ""
    elif c == "-":      # 뺄셈
        cal_queue.append(int(current_target[::-1])+sum(sum_queue))
        sum_queue.clear()
        current_target = ""
else:
    cal_queue.append(int(current_target[::-1])+sum(sum_queue))

# 최종 계산
output = cal_queue.pop()
for num in cal_queue[::-1]:
    output -= num

print(output)       # 출력
