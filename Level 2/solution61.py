# 코딩테스트 연습 / 연습문제 / 2 x n 타일링
# 규칙을 발견하고 피보나치의 방식으로 문제를 풀이함

def solution(n):
    maxNum = 1000000007
    answer = []
    answer.extend([1,2])
    
    for _ in range(3, n+1):
        answer.append(sum(answer[-2:])%maxNum)
    
    return answer[-1]%maxNum


print(solution(4))          # 5
print(solution(7))          # 21

'''
    < 처음 풀이 >
    # 시간 초과 발생, 규칙상 피보나치 수열과 알고리즘이 동일하게 나타남
    def solution(num):
        answer = 0
        comb = [[0 for _ in range(num+1)] for _ in range(num+1)]
        
        
        # 파스칼 삼각형 미리 구하기
        for n in range(num+1):
            for r in range(num+1):
                if n<r: break
                elif r==0 or n==r:    comb[n][r] = 1
                else:
                    comb[n][r] = comb[n-1][r] + comb[n-1][r-1]
        
        two, one = divmod(num,2)
        n, r = two+one, two
        
        while r >= 0:
            answer += comb[n][r]
            n, r = n+1, r-1
        
        return answer%1000000007
        
    < 다른 풀이 >
    # 피보나치로 풀긴 했는데 코드를 되게 pythonic 하게 짬
    def tiling(n):
        a,b=1,1
        for i in range(n):a,b=b,a+b
        return a%100000
'''