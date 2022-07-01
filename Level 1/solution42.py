# 코딩테스트 연습 / 연습문제 / 자릿수 더하기

def solution(n):
    answer = 0

    for num in map(int,str(n)):
        answer += num

    return answer

'''
    < 다른 풀이 >
    # sum 활용
    return sum([int(i) for i in str(number)])
'''