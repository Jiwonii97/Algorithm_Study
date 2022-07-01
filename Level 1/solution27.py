# 코딩테스트 연습 / 연습문제 / 가운데 글자 가져오기

def solution(s):
    if len(s) % 2 != 0:
        return s[len(s)//2]
    else:
        return s[len(s)//2-1:len(s)//2+1]
    
'''
    < 다른 풀이 >
    # slicing 사용
    return str[(len(str)-1)//2:len(str)//2+1]
'''