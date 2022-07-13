# 코딩테스트 연습 / 완전탐색 / 모음사전

from itertools import product

def solution(word):
    words = [""]
    
    # 중복순열을 통해 전체 리스트를 만들고 정렬 후 직접 탐색
    for i in range(1, 6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words.append(''.join(list(c)))

    return sorted(words).index(word)

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))

'''
    < 다른 풀이 >
    # 등비수열의 합 활용
    # https://hzoo.tistory.com/12
    
    def solution(word):
        answer = 0
        for i, n in enumerate(word):
            answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
        return answer
'''