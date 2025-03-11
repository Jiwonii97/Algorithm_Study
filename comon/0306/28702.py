# https://www.acmicpc.net/problem/28702
# FizzBuzz
# 문자열 문제, 문자에서 숫자를 찾아 다음 숫자를 예측해 변환 (O(1))

import sys

texts = [sys.stdin.readline().strip() for _ in range(3)]
target = 0

for idx, text in enumerate(texts[::-1]):
    if text.isdigit():
        target = int(text)+(idx+1)

if target%15==0:
    print("FizzBuzz")
elif target%3==0:
    print("Fizz")
elif target%5==0:
    print("Buzz")
else:
    print(target)