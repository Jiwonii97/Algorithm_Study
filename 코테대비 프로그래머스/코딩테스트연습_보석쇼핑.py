# https://school.programmers.co.kr/learn/courses/30/lessons/67258

# 투포인트 + 딕셔너리를 통한 현황 유지
'''
    딕셔너리를 이용해 해시를 활용하여 전체 리스트의 키를 확보하고
    투포인트를 사용해 조건에 맞도록 조절하고 있다.
'''


def solution(gems):
    from collections import defaultdict
    answer = [0, len(gems)-1]
    jw = defaultdict(lambda: 0)

    kindsGems = len(set(gems))

    jw[gems[0]] += 1
    start, end = 0, 0
    while start < len(gems) and end < len(gems):
        if len(jw.keys()) < kindsGems:
            end += 1
            if end == len(gems):
                break

            jw[gems[end]] += 1
        else:
            if (end-start+1) < (answer[1]-answer[0]+1):     # 지금꺼가 더 짧음
                answer = [start, end]
            if jw[gems[start]] == 1:        # 한개 남은 경우, 이거빼면 전체 종류가 바뀜
                del jw[gems[start]]
            else:               # 그 외의 경우는 전체 개수를 하나 뻄
                jw[gems[start]] -= 1
            start += 1
    answer = [answer[0]+1, answer[1]+1]
    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA",
      "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))

'''
    def solution(gems):
        kindsGems = len(set(gems))

        for leng in range(kindsGems, len(gems)+1):
            for idx in range(len(gems)-leng+1):
                if len(set(gems[idx:idx+leng])) == kindsGems:
                    return [idx+1, idx+leng]
                
    def solution(gems):
        answer = []
        kindsGems = len(set(gems))

        for idx in range(len(gems)-kindsGems+1):
            for leng in range(kindsGems, len(gems)-idx+1):
                if len(set(gems[idx:idx+leng])) == kindsGems:
                    answer.append([leng, [idx+1, idx+leng]])

        answer.sort()
        return answer[0][1]
'''
