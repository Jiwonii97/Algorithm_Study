# 코딩테스트 연습 / 2021 Dev-Matching: 웹 백엔드 개발자(상반기) / 로또의 최고 순위와 최저 순위
# 단순 수학 문제

def solution(lottos, win_nums):       
    lottos.sort()
    win_nums.sort()
    
    cnt0 = lottos.count(0)
    lottos = list(set(lottos))
    
    if 0 in lottos:
        lottos.remove(0)
        
    point = 0
    for x in lottos:
        if x in win_nums:
            point += 1

    minpoint = 7-point
    maxpoint = minpoint - cnt0
    
    if minpoint >= 6:
        minpoint = 6
    if maxpoint >= 6:
        maxpoint = 6

    return [maxpoint,minpoint]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))
print(solution([1,2,3,4,5,6],[7,8,9,10,11,12]))

'''
< 다른 풀이 >
def solution(lottos, win_nums):
    
    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
'''