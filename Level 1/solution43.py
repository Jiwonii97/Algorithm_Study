# 코딩테스트 연습 / 연습문제 / 자연수 뒤집어 배열로 만들기

def solution(n):    
    return [int(num) for num in list(str(n))][::-1]

'''
    < 다른 풀이 >
    # map으로 문자열을 숫자로 변환
    # reversed로 문자열 뒤집기 활용
    return list(map(int, reversed(str(n))))
'''