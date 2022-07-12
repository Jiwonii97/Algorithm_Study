# 코딩테스트 연습 / 완전탐색 / 피로도
# 순열을 통해 모든 경우의 수를 구하고 전체의 경우의 수를 탐색

def solution(k, dungeons):
    answer = -1
    
    from itertools import permutations
    tasks = permutations(dungeons,len(dungeons))
    
    for task in tasks:
        cnt=0;  hp = k
        for dungeon in task:
            if hp >= dungeon[0]:
                cnt+=1; hp -= dungeon[1]
                
        if answer < cnt:
            answer = cnt
    
    return answer

print(solution(80,[[80,20],[50,40],[30,10]]))