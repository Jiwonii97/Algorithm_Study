# 코딩테스트 연습 / 2022 KAKAO BLIND RECRUITMENT / k진수에서 소수 개수 구하기
# 문자열 단순 구현 문제, 시간초과 문제때문에 처음엔 고생하였지만 여러번의 경우를 탐지하는 경우에는 DP 방식보다는 단순 방법이 더 효율적이었던거 같다.

def solution(n, k):
    answer = 0
    
    # k진수 수로 변환
    pn = ""
    while n > 0:
        n, mod = divmod(n,k)
        pn += str(mod)
    pn = pn[::-1]     # ''.join(reversed(pn))
    
    # 소수 찾기
    number = list(map(int,[x for x in pn.split('0') if str.isdigit(x)]))
    
    for num in number:
        # 1은 소수가 아니다
        if num == 1:
            continue
        for n in range(2, int(num**(1/2))+1):
            if num%n == 0:
                break
        else:
            answer += 1
    
    return answer

print(solution(437674,3))	        # 3
print(solution(110011,10))	        # 2

'''
    < 처음 풀이 >
    # 시간초과가 계속 발생, 제곱근으로 해도 시간초과가 나는걸 보면 DP를 사용해서 미리 리스트를 뽑아서 계산하는게 아니라 실시간으로 계산하는게 더 빠르다고 봄
    # 전체적인 리스트를 뽑는게 아니라 "맞는지틀리는지" 만 확인하는거면 실시간이 더 좋은듯
    def solution(n, k):
        answer = 0
    
        # k진수 수로 변환
        pn = ""
        while n > 0:
            n, mod = divmod(n,k)
            pn += str(mod)
        pn = pn[::-1]     # ''.join(reversed(pn))
        
        # 소수 찾기
        number = list(map(int,[x for x in pn.split('0') if str.isdigit(x)]))
        maxNum = max(number)
        
        primeNum = set(range(2,maxNum+1))
        for i in range(2, int(maxNum**(1/2))+1):
            if i in primeNum:
                primeNum-=set(range(2*i,maxNum+1,i))
        
        for num in number:
            # 연속적으로 0이 나올수 있기 때문에 공백이 생길수 있어 해당 문자열이 숫자형태인지 우선 확인후 미리 찾아둔 리스트에서 소수 찾기
            if num in primeNum:
                answer += 1
    
    return answer
'''