# 코딩테스트 연습 / 연습문제 / 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    return sorted([x for x in arr if x%divisor == 0]) if len(sorted([x for x in arr if x%divisor == 0])) != 0 else [-1]

'''
    < 다른 풀이 >
    # or을 사용하여 리스트에 아무것도 없으면 [-1]이 포함
    return sorted([n for n in arr if n%divisor == 0]) or [-1]
'''