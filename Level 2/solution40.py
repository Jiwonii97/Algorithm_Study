# 코딩테스트 연습 / 연습문제 / 다음 큰 숫자

from collections import Counter
def solution(n):
        
    one_count = Counter(list(bin(n)[2:]))['1']
    start = n+1
    while True:
        target = Counter(list(bin(start)[2:]))['1']
        if target == one_count:
            break
        
        start += 1
    
    return start

# 출력
print(solution(78))         # 83
print(solution(15))         # 23

'''
    < 다른 풀이 >
    # 굳이 Counter를 사용하지 않아도 string 자체의 count를 활용해 원하는 값을 찾을 수 있음
    def nextBigNumber(n):
        num1 = bin(n).count('1')
        while True:
            n = n + 1
            if num1 == bin(n).count('1'):
                break
        return n
'''