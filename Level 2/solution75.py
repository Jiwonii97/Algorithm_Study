# 코딩테스트 연습 / 연습문제 / 할인 행사

def solution(want, number, discount):

    purchase = []
    for w, n in zip(want, number):
        purchase.extend([w]*n)

    psize = sum(number)
    purchase.sort()

    for idx in range(len(discount)-psize+1):
        dis = sorted(discount[idx:idx+psize])

        for p, d in zip(purchase, dis):
            if p != d:
                break

        else:
            return idx+1

    return 0


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple",
      "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))       # 3
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana",
      "banana", "banana", "banana", "banana", "banana", "banana"]))      # 0

'''
    < 다른 풀이 >
    def solution(want, number, discount):
        from collections import Counter
        answer = 0

        purchase = set((x, y) for x, y in zip(want, number))
        psize = sum(number)

        for idx in range(len(discount)-psize):
            dis = discount[idx:idx+psize]
            disList = set(Counter(dis).most_common())

            if not (purchase - disList):
                answer = idx+1
                break
        else:
            return 0

        return answer
'''
