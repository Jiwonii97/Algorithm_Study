# 코딩테스트 연습 / 연습문제 / 소수 찾기
# 에라토스테네스의 체

def solution(n):    
    a = [False,False] + [True]*(n-1)
    primes=[]
    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    
    return len(primes)

'''
    < 다른 풀이 >
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
'''