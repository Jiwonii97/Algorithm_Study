# 코딩테스트 연습 / 연습문제 / 시저 암호
# 나머지 연산 활용
# chr : char형 타입, ord : 아스키코드 번호

def solution(s, n):
    answer = ''
    big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small = big.lower()
    
    for text in list(s):
        if text.isupper():
            idx = big.index(text)+n
            if idx >= 26:
                idx-=26
            text=big[idx]
        elif text.islower():
            idx = small.index(text)+n
            if idx >= 26:
                idx-=26
            text=small[idx]
        answer += text
            
    return answer

'''
    < 다른 풀이 >
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
'''