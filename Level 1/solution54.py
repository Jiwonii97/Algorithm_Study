# 코딩테스트 연습 / 연습문제 / x만큼 간격이 있는 n개의 숫자
# list comprehension

def solution(x, n):
    answer = []
    for n in range(0,n):
        answer.append(x+x*n)
    return answer

'''
    < 다른 풀이 >
    return [i * x + x for i in range(n)]
'''