# 코딩테스트 연습 / 연습문제 / 제일 작은 수 제거하기

def solution(arr):
    idx_ = 0
    min_ = 999999999
    for n in range(len(arr)):
        if min_>arr[n]:
            min_ = arr[n]
            idx_ = n
            
    arr.pop(idx_)
    
    return arr if len(arr) != 0 else [-1]

'''
    < 다른 풀이 >
    # lambda 함수 활용
    solution=lambda _:fi if _.remove(min(_)) else (len(_) and _ or [-1])
'''