# 코딩테스트 연습 / 연습문제 / 줄 서는 방법
# 기존 순열을 구하는 과정에서 일일이 구하고 결과를 출력하는 방식은 시간초과가 발생하지만 직접 연산을 통해 구하는 방식은 더 좋은 효율성을 보여줌

from math import factorial
def solution(n, k):
    answer = []
    number = list(range(1,n+1)) 
    step = n-1
    while number:
        idx = 0
        
        while k > factorial(step):
            k -= factorial(step)
            idx += 1

        answer.append(number.pop(idx))
        step -= 1
    
    return answer

print(solution(3,5))        # [3,1,2]
print(solution(4,10))        # [2,3,4,1]

'''
    < 처음 풀이 >
    # 효율성 테스트 전부 실패
    from itertools import permutations
    def solution(n, k):    
        answer = permutations(range(1,n+1),n)
        return list(list(answer)[k-1])
        
        
    < 다른 풀이 >
    # 하나씩 빼는게 아닌 나머지 연산 활용    
    def solution(n, k):
        from math import factorial
        answer = []
        order = list(range(1,n+1))
        while n!=0 :
            fact = factorial(n-1)
            answer.append(order.pop((k-1)//fact))
            n,k = n-1, k%fact
        return answer
'''