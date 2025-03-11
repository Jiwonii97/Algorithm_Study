# https://www.acmicpc.net/problem/1541
# 잃어버린 괄호
# 수식의 뒤 부터 덧셈이 붙은 숫자는 더해 큰수로 큐에 저장해두어 덧셈을 계산하고, 이를 계산 큐에 넣어 최종적으로 제일 앞에 있는 숫자에 대해 뒤에 큰수들을 빼는 방식으로 최소값을 구함

'''
    예시 : 
        1)  55-50+40
            -35
        2)  10+20+30+40
            100
        3)  00009-00009
            0
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
