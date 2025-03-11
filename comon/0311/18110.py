# https://www.acmicpc.net/problem/18110
# solved.ac
# round 함수는 우리가 아는 반올림과 다르게 실행됨 (O(n))

import sys

def round(n):
    return int(n)+1 if n-int(n) >= 0.5 else int(n)

n = int(sys.stdin.readline().strip())
if n==0:
    print(0)
else:
    count = round(n*0.15)
    
    case = []
    for _ in range(n):
        case.append(int(sys.stdin.readline().strip()))
    case = sorted(case)
    
    target = case[count:len(case)-count]

    print(round(sum(target)/len(target)))