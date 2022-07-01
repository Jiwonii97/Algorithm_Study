# 코딩테스트 연습 / 연습문제 / 피보나치 수

def solution(n):
    fibo = [0,1]+[0]*(100000-1)
    for idx in range(2,n+1):
        fibo[idx] = fibo[idx-1] + fibo[idx-2]
    
    return fibo[n]%1234567

'''
    < 다른 풀이 >
    def fibonacci(num):
        a,b = 0,1
        for i in range(num):
            a,b = b,a+b
        return a
'''