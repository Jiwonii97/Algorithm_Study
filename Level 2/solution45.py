# 코딩테스트 연습 / 월간 코드 챌린지 시즌1 / 이진 변환 반복하기

def solution(s):    
    zero, cnt = 0, 0
    
    while len(s) > 1:
        tmp = s.replace("0","")
        zero += len(s) - len(tmp)
        s = bin(len(tmp))[2:]
        cnt += 1
    
    return [cnt,zero]

print(solution("110010101001"))         # [3,8]
print(solution("01110"))            # [3,3]
print(solution("1111111"))          # [4,1]

'''
    < 다른 풀이 >
    # s.count('1')로 1의 개수를 확인 가능
    
    # from collections import Counter
    # Counter(s)['1'] 을 통해 1의 개수 확인 가능
'''