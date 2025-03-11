# https://www.acmicpc.net/problem/9935
# 문자열 폭발
# stack을 활용한 문제 풀이법
# TIL: pop()이 slice후 다시 대입하는 거 보다 더 시간이 적음

import sys

string = sys.stdin.readline().strip()
target = sys.stdin.readline().strip()

stack = []
for s in string:
    # 스택에 넣기
    stack.append(s)

    # 글자수를 넘지 못하면 push만 진행
    if len(stack) < len(target):
        continue
    
    # 뒤부터 길이 만큼 긁어서 같으면 pop()
    if stack[-len(target):] == list(target):
        for _ in range(len(target)):
            stack.pop()

print(''.join(stack) if stack else "FRULA")