# 코딩테스트 연습 / 스택/큐 / 주식가격

def solution(prices):
    lengths = len(prices)
    answer = [0]*lengths
    stacks = []
    
    for idx, data in enumerate(prices):
        while stacks and data < prices[stacks[-1]]:
            idx2 = stacks.pop()
            answer[idx2] = idx - idx2
        stacks.append(idx)
        
    while stacks:
        idx3 = stacks.pop()
        answer[idx3] = lengths - (idx3 + 1)
    
    return answer

print(solution([1, 2, 3, 2, 3]))

'''
    < 다른 풀이 > - 브루트포스(완전탐색) / 스택과 비교하면 많이 느림 (O(N^2))
    def solution(prices):
        answer = [0] * len(prices)
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] <= prices[j]:
                    answer[i] += 1
                else:
                    answer[i] += 1
                    break
        return answer
        
    < 다른 풀이 > - deque로 스택같이 품
    from collections import deque
    def solution(prices):
        answer = []
        prices = deque(prices)
        while prices:
            c = prices.popleft()

            count = 0
            for i in prices:
                if c > i:
                    count += 1
                    break
                count += 1

            answer.append(count)

        return answer
'''