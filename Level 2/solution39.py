# 코딩테스트 연습 / 2022 KAKAO BLIND RECRUITMENT / 양궁대회

from itertools import combinations_with_replacement as cwr
def solution(n, apeachs):
    answer = [-1]
    gap = -1
    
    combs = cwr(range(11),n)
    
    for comb in combs:
        # 라이언이 맞춘 과녁
        lions = [0]*11
        
        # 맞힌 화살 개수 확인
        for c in comb:
            lions[10-c] += 1
    
        apeach, lion = 0, 0
        for idx in range(10+1):
            # 둘다 못맞추었으면 일단 통과
            if apeachs[idx] == 0 and lions[idx] == 0:
                continue
            # 나머지 점수추가는 알아서
            elif apeachs[idx] >= lions[idx]:
                apeach += (10-idx)
            else:
                lion += (10-idx)
                
        if lion > apeach:
            if gap < lion-apeach:
                gap = lion-apeach
                answer = lions
    return answer
	

print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))      # [0,2,2,0,1,0,0,0,0,0,0]
print(solution(1,[1,0,0,0,0,0,0,0,0,0,0]))      # [-1]
print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]))      # [1,1,2,0,1,2,2,0,0,0,0]
print(solution(10,[0,0,0,0,0,0,0,0,3,4,3]))     # [1,1,1,1,1,1,1,1,0,0,2]


'''
    < 다른 풀이>
    # dfs를 사용하지 않은 나와 유사한 방식이지만 Counter를 써서 원소의 개수를 바로 확인하여 좀더 코드를 용이하게 짬
    from itertools import combinations_with_replacement
    from collections import Counter
    def solution(n, info):
        maxdiff,max_comb=0,{}
        for combi in combinations_with_replacement(range(11), n):
            cnt=Counter(combi)
            score1, score2=0,0
            for i in range(1, 11):
                if info[10-i]<cnt[i]: score1+=i
                elif info[10-i]>0: score2+=i
            diff=score1-score2
            if diff>maxdiff:
                max_comb=cnt
                maxdiff=diff
        if maxdiff>0:
            answer=[0]*11
            for n in max_comb:
                answer[10-n]=max_comb[n]
            return answer
        else: return [-1]
        
    # dfs를 활용하여 풀이한 문제
    def solution(n, info):
        global answer, result

        # 점수 계산 함수
        def score(ryan):
            s = 0
            for i in range(11):
                if ryan[i] == info[i] == 0:
                    continue
                if ryan[i] > info[i]:
                    s += 10 - i
                else:
                    s -= 10 - i
            return s

        def dfs(idx, left, ryan):
            global answer, result
            if idx == -1 and left:
                return
            if left == 0:
                s = score(ryan)
                if result < s:
                    answer = ryan[:]
                    result = s
                return
            for i in range(left, -1, -1):
                ryan[idx] = i
                dfs(idx-1, left-i, ryan)
                ryan[idx] = 0

        answer = [0 for _ in range(11)]
        result = 0
        dfs(10, n, [0 for _ in range(11)])
        return answer if result != 0 else [-1]
'''