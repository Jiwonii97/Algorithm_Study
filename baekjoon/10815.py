# https://www.acmicpc.net/problem/10815
# 숫자 카드

in_count = int(input())
_dict = {x: True for x in input().split()}

out_count = int(input())

for x in input().split():
    if x in _dict.keys():
        print(1, end=" ")
    else:
        print(0, end=' ')
