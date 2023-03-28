# https://school.programmers.co.kr/learn/courses/30/lessons/64064
# 정규식, 순열 문제풀이

def solution(user_id, banned_id):
    from itertools import permutations
    import re
    answer = 0

    cases = permutations(user_id, len(banned_id))
    done = []

    for case in cases:
        for pm, ban in zip(case, banned_id):
            if len(pm) != len(ban):     # 길이가 다른 경우
                break

            ptrn = ban.replace('*', '\\w')  # 정규식 패턴 설정
            p = re.compile(f"{ptrn}")

            # ptrn = ban.replace('*', '\w')  # 정규식 패턴 설정
            # p = re.compile(r"{}".format(ptrn))

            if p.match(pm) == None:
                break
        else:
            newCase = sorted(list(case))        # 중복 제거
            if newCase not in done:
                answer += 1
                done.append(newCase)

    return answer


print(solution(["frodo", "fradi", "crodo",
      "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123",
      "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
      ["fr*d*", "*rodo", "******", "******"]))
