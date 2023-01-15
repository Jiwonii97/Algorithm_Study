# 코딩테스트 연습 / 2021 KAKAO BLIND RECRUITMENT / 메뉴 리뉴얼
# Counter().most_common()으로 (최대 빈도의 값, 개수)를 확인할 수 있음
# 문자열 + 구현 문제, 이전 문제와 유사한 문제, 전체적인 경우의 수를 구하고 개수를 확인해 최대값을 찾아 활용하는 문제, for문으로 어느 경우까지 범위를 제한하는게 필요 요소 중 하나라고 생각

from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []

    for c in course:
        menu_list = []
        for order in orders:
            course_menu = combinations(list(order), c)
            for menu in course_menu:
                menu_list.append(''.join(sorted(menu)))

        result = Counter(menu_list)
        if result:
            maximum = max(result.values())
            if maximum >= 2:
                filtered = [x for x, v in result.items() if v == maximum]

                answer.extend(filtered)
        else:
            continue

    return sorted(answer)


# ["AC", "ACDE", "BCFG", "CDE"]
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
# ["ACD", "AD", "ADE", "CD", "XYZ"]
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))       # ["WX", "XY"]
