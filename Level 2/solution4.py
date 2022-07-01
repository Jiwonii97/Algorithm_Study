# 코딩테스트 연습 / 연습문제 / 행렬의 곱셈

def solution(arr1, arr2):
    import numpy as np
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    return np.dot(arr1,arr2).tolist()


'''
< 다른 풀이 >
# Asterisk(*)을 언패킹 컨테이너로 사용 - 이차원 리스트로 선언된 B를 언패킹하여 1차원으로 만들고 zip하여 열로 나타냄
def solution(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
    
a = [ [ 1, 2 ], [ 2, 3 ]]
b = [[ 3, 4], [5, 6]]
print("결과 : {}".format(solution(a,b)))
'''