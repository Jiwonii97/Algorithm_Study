# 코딩테스트 연습 / 연습문제 / 최대공약수와 최소공배수

def gcd(m,n):
    return m if n==0 else gcd(n,m%n)

def lcm(m,n):
    return int(m*n/gcd(m,n))

def solution(n, m):
    return [gcd(n,m),lcm(n,m)]

'''
    < 다른 풀이 >
    gcd = lambda a,b : b if not a%b else gcd(b, a%b)
    lcm = lambda a,b : a*b//gcd(a,b)
    return [gcd(n, m), lcm(n, m)]
'''