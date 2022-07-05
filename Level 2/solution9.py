# 코딩테스트 연습 / 정렬 / H-Index

def solution(citations):
    answer = 0
    citations = sorted(citations)
    check = list(range(citations[-1]+1))
    total_size = len(citations)
    
    for hindex in check:
        length_ = len([x for x in citations if x>=hindex])
        if length_ >= hindex and  hindex >= total_size-length_ :
            answer = hindex
        # print("{}편의 논문은 {}회 이상이 인용, 나머지 {}편의 논문은 {}회 이하 인용".format(hindex,length_, total_size-length_, hindex))
    return answer
        
print(solution([3, 0, 6, 1, 5]))
print(solution([0,0,0,0,0,0]))

'''
    < 다른 풀이 > - sort와 map 활용
    def solution(citations):
        citations.sort(reverse=True)
        answer = max(map(min, enumerate(citations, start=1)))
        return answer
        
    < 다른 풀이 > - 내가 푼것보다 더 간결함
    def solution(citations):
        citations = sorted(citations)
        l = len(citations)
        for i in range(l):
            if citations[i] >= l-i:
                return l-i
        return 0
'''