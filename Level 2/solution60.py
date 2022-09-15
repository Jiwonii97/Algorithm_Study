# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [3차] n진수 게임
# 문자열 문제, 진수 변환을 활용, 조건에 맞도록 문자열을 걸러냄

def jinsu(n, k):
    character = {idx:x for idx,x in enumerate("0123456789ABCDEF")}
    result = []
    # 0은 그냥 출력
    if n==0: return 0
    
    # 10진수 -> k진수로 변환
    while n != 0:
        n, mod = divmod(n,k)
        result.append(character[mod])
        
    return ''.join(result)[::-1]

def solution(n, t, m, p):
    answer = ''
    maxNum = 100000
    
    for num in range(maxNum):
        tmp = jinsu(num,n)
        
        answer += str(tmp)
        if len(answer) >= t*m:
            break
    
    return ''.join([x for idx, x in enumerate(answer) if idx%m == p-1])[:t]

print(solution(2,4,2,1))        # "0111"
print(solution(16,16,2,1))      # "02468ACE11111111"
print(solution(16,16,2,2))      # "13579BDF01234567"

'''
    <다른 풀이>
    answer = a[p-1::m][:t]
    # join과 조건문을 사용한 내 방식과 달리 slicing 자체를 활용하는 방법도 있다
'''