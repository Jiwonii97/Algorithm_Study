# 코딩테스트 연습 / Summer/Winter Coding(~2018) / 소수 만들기

def solution(nums):
    answer = 0

    aratos = {x:True for x in range(1,1000+1)}
    aratos[1] = False
    
    # 에라토스테네스 체로 소수를 먼저 구함
    for num in aratos.keys():
        if aratos[num]:
            for idx in range(num+num,1000,num):
                aratos[idx] = False
            
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if aratos[nums[i] + nums[j] + nums[k]]:
                    answer += 1

    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))

'''
< 다른 풀이 >
# 모든 조합의 경우를 구해주는 함수 : from itertools import combinations -> list(combinations(nums, 3))

def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
            else:
                answer += 1
    return answer
'''