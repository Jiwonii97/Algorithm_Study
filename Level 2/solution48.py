# 코딩테스트 연습 / 연습문제 / N개의 최소공배수
# gcd/lcm 함수를 직접 만들어서 원하는 값을 추출
# 자동으로 정렬을 진행해 작은 수 부터 lcm을 구하는 방식 진행하였지만, 굳이 그래야 하나 싶긴함

def solution(arr):

    gcd = lambda a,b : b if not a%b else gcd(b, a%b)
    lcm = lambda a,b : a*b//gcd(a,b)
    import heapq
    
    heapq.heapify(arr)   
    
    while len(arr) > 1:
        n1 = heapq.heappop(arr)
        n2 = heapq.heappop(arr)
        heapq.heappush(arr, lcm(n1, n2))
    
    return arr[-1]

print(solution([2,6,8,14]))         # 168
print(solution([1,2,3]))            # 6


'''
    < 다른 풀이 >
    # gcd 라이브러리를 직접사용하였지만 실제 코테에서는 사용가능한지 의문이긴함
    from fractions import gcd
    def nlcm(num):      
        answer = num[0]
        for n in num:
            answer = n * answer / gcd(n, answer)

        return answer

'''