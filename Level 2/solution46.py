# 코딩테스트 연습 / 연습문제 / 숫자의 표현
# 완전 탐색으로 푸는 문제
# 왜 이렇게 간단하게 푸는 방법이 있는데 복잡하게 접근 했을까.. 아마 sum에서 매번 작업을 해야하니 효율성 에러가 났다고 생각

def solution(n):    
    answer = 0
    for i in range(1, n//2+1):
        sum = 0
        for j in range(i, n+1):
            sum += j
            if sum == n:
                answer += 1
                break
            elif sum > n:
                break
            
    return answer

print(solution(15))         # 4

'''
    < 효율성 테스트 실패 >
    def solution(n):
        answer = 0
        number = list(range(1,n+1))
        
        for size in range(1,(n+1)//2):
            
            # 더이상 찾을 수 없음
            if sum(number[:size]) > n:
                break
            
            for i in range(n-size+1):
                if sum(number[i:i+size]) == n:
                    answer += 1
                    break
        
        return answer
        
    < 다른 풀이 1>
    # n = (p) = p = n
    # n = (k) + (k+1) = 2k + 1 = 2k + sum(1,2)
    # n = (l) + (l+1) + (l+2) = 3l + 1 + 2 = 3l + sum(1,3)
    # n = (m) + (m+1) + (m+2) + (m+3) = 4m + 1 + 2 + 3 = 4m + sum(1,4)
    # 이와 같은 규칙을 확인하고 푸는 방식
    
    def solution(n):
        answer = 1
        for i in range(2,n+1):
            div, mod = divmod(n-sum(range(1,i)),i)
            if div <= 0:
                break
            if mod == 0:
                answer += 1
                
        return answer
    
    
    < 다른 풀이 2>
    # 주어진 자연수를 연속된 자연수의 합으로 표현하는 방법의 수는 주어진 수의 홀수 약수의 개수와 같다
    def expressions(num):
        return len([i  for i in range(1,num+1,2) if num % i is 0])
        
    - 연속된 정수의 합
    a + (a+1) + (a+2) + ... + (a+k-1) = k(2a+k-1)/2 = n
    a = n/k + (1-k)/2
    
    위 조건을 만족 하려면
    1. n/k 가 자연수이려면 : k는 n의 약수여야 한다.
    2. (1-k)/2 가 정수가 되려면 : 1-k 가 짝수여야 하므로 k는 홀수여야 한다.
    3. k < n
    
    위 세가지 조건을 만족해야 하므로 n의 약수 중 홀수인 수를 찾으면 된다
'''