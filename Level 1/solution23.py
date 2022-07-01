# 코딩테스트 연습 / 위클리 챌린지 / 최소직사각형

def solution(sizes):
    w,h = 0,0
    
    for size in sizes:
        tmp1, tmp2 = sorted(size)
        w = max(w,tmp1)
        h = max(h,tmp2)
    
    return w*h

'''
    < 다른 풀이 >
    # min, max를 활용한 수학 구현 문제
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
'''