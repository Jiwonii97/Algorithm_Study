# 코딩테스트 연습 / 연습문제 / 하샤드 수

def solution(x):
    cal = 0
    for num in list(str(x)):
        cal+=int(num)
    return x%cal == 0

'''
    < 다른 풀이 >
    # sum 활용
    return n % sum([int(c) for c in str(n)]) == 0
'''