# 코딩테스트 연습 / 연습문제 / 행렬의 덧셈

def solution(arr1, arr2):
    import numpy as np
    answer = np.array(arr1)+np.array(arr2)
    return answer.tolist()

'''
    < 다른 풀이 >
    # zip과 리스트를 활용한 문제
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer
'''