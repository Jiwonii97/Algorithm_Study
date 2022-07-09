# 코딩테스트 연습 / 완전탐색 / 소수 찾기

def solution(numbers):
    from itertools import permutations
    num_max = int("9"*len(numbers))+1
    answer = []
    
    # num : 소수 리스트
    num=set(range(2,num_max))
    for i in range(2,num_max):
        if i in num:
            num-=set(range(2*i,num_max,i))
    
    numbers = list(numbers)
    print(numbers)
    
    for size in range(1,len(numbers)+1):
        tasks = permutations(numbers,size)
        for task in tasks:
            nb = int("".join(task))
            if nb in num:
                answer.append(nb)
        
    return len(set(answer))

print(solution("17"))
print(solution("011"))

'''
    < 다른 풀이 >
    from itertools import permutations
    def solution(n):
        a = set()
        for i in range(len(n)):
            a |= set(map(int, map("".join, permutations(list(n), i + 1))))
        a -= set(range(0, 2))
        for i in range(2, int(max(a) ** 0.5) + 1):
            a -= set(range(i * 2, max(a) + 1, i))
        return len(a)
'''