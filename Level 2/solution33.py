# 코딩테스트 연습 / Summer/Winter Coding(2019) / 멀쩡한 사각형

def solution(w,h):
    from math import ceil, floor
    
    # 예외 처리
    if w == h:
        return w*h - w
    elif w == 1 or h == 1:
        return 0
    
    # 최대 공약수를 찾아 효율적으로 검색
    m, n = w, h
    while n != 0:
        tmp = n
        n = m%tmp
        m = tmp
        
    wmin, hmin = w//m, h//m
    
    grad = hmin/wmin
    f = lambda x : grad*x
    cnt, start = 0, 0
    
    for xpos in range(1,wmin+1):            
        ypos = f(xpos)
        cnt += ceil(ypos)-start
        start = floor(ypos)
    
    return w*h-cnt*m

print(solution(8,12))

'''
    < 다른 풀이 >
    from math import gcd
    def solution(w,h):
        return w * h - (w/gcd(w, h) + h/gcd(w, h) - 1) * gcd(w, h)
        # return w * h - (w + h - gcd(w, h))
'''