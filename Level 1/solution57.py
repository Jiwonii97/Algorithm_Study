# 코딩테스트 연습 / 연습문제 / 햄버거 만들기


def solution(ingredient):
    answer = 0
    hamburger = [1, 2, 3, 1]
    st = []

    for i in ingredient:
        st.append(i)
        if len(st) < 4:
            continue
        else:
            if st[-4:] == hamburger:
                answer += 1
                del st[-4:]
    return answer


print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))        # 2
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))        # 0
