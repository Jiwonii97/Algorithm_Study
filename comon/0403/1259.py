# https://www.acmicpc.net/problem/1259
# 팰린드롬수
# 문자열, [::-1]로 텍스트 역순을 취해서 String 비교
# O(N)

import sys

input = sys.stdin.readline

while True:
    text = input().strip()

    if text == '0':
        break

    print("yes" if text == text[::-1] else "no")