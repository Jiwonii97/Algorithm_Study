# 코딩테스트 연습 / 연습문제 / 옹알이(2)

def solution(babbling):
    answer = 0

    for bab in babbling:
        # 1. 연속 먼저 체크
        if bab != bab.replace("ayaaya", "").replace("yeye", "").replace("woowoo", "").replace("mama", ""):
            continue

        if bab.replace("aya", " ").replace("ye", " ").replace("woo", " ").replace("ma", " ").strip() == "":
            answer += 1

    return answer


print(solution(["aya", "yee", "u"]))        # 1
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))     # 2
