# 코딩테스트 연습 / 2021 KAKAO BLIND RECRUITMENT / 순위 검색
# 구현 및 정렬/탐색 문제, 카카오 코테 다운 문제로 효율성을 위해 이진탐색을 사용하여 효율을 높임, 정렬을 진행하지 않으면 탐색 과정에서 시간초과가 발생한다
# 전체적인 케이스를 확인하고 전체의 경우를 미리 구하고 문제를 푸는것이 더 빨리 풀수 있는 문제

from collections import defaultdict
from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    answer = []
    conditions_list = defaultdict(list)

    # 경우의 수 마련
    for i in info:
        conditions = i.split(' ')[:-1]
        score = i.split(' ')[-1]

        for size in range(4+1):
            for comb in combinations(conditions, size):
                keys = ''.join(comb)
                conditions_list[keys].append(int(score))

    for key in conditions_list:
        conditions_list[key].sort()

    # query 분석
    for q in query:
        subquery = [x for x in q.split(' ') if x != "and" and x != "-"]
        conditions, target = subquery[:-1], subquery[-1]
        query_key = ''.join(conditions)

        if query_key in conditions_list:

            scores = conditions_list[query_key]
            if scores:  # score리스트에 값이 존재하면
                pivot = bisect_left(scores, int(target))        # 자기보다 큰수의 개수
                answer.append(len(scores) - pivot)
        else:
            answer.append(0)

    return answer


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
                "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
               ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250",
                "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))

'''
    # 시간 초과
    from collections import defaultdict
    def solution(info, query):
        answer = []
        keywords = defaultdict(list)

        # [java/python/cpp, fe/be, junior/senior, chicken/pizza , 1~100000]
        appliants = [i.split(' ') for i in info]

        # 딕셔너리에 저장
        for idx, appliant in enumerate(appliants):
            for app in appliant[:-1]:
                keywords[app].append(idx)
            keywords['points'].append([int(appliant[-1]), idx])

        # 쿼리문 문석
        for q in query:
            sets = None
            keys = q.replace('and ', '').split(' ')

            # 쿼리 분석
            for key in keys[:-1]:
                if key == '-':
                    continue
                elif sets is None:
                    sets = set(keywords[key])
                else:
                    sets = sets & set(keywords[key])

            # 마지막으로 점수 분석
            sets = sets & set([x[1] for x in keywords['points'] if x[0] >= int(
                keys[-1])]) if sets is not None else set([x[1] for x in keywords['points'] if x[0] >= int(keys[-1])])
            answer.append(len(sets))

        return answer
'''
