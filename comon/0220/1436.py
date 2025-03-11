# https://www.acmicpc.net/problem/1436
# 영화감독 숌
#

'''
    예시 : 
        2
        1666
        
        3
        2666
        
        6
        5666

        187
        66666
'''

import sys
count = int(sys.stdin.readline().strip())

target = 0
for i in range(666, 99999999):
    if '666' in str(i):
        target += 1

    if target == count:
        target = i
        break

print(target)
