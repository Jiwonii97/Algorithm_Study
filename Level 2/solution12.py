# 코딩테스트 연습 / 해시 / 위장
# (a+1)(b+1)(c+1) = abc + ab + ac + bc + a + b + c + 1 의 수식을 활용

def solution(clothes):
    answer = 1
    dict_clothes = {}
    
    for cloth in clothes:
        if cloth[1] in dict_clothes.keys():
            dict_clothes[cloth[1]] += 1
        else:
            dict_clothes[cloth[1]] = 1
            
    cloth = dict_clothes.values()
    for num in cloth:
        answer *= (num+1)
            
    return answer-1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))

'''
    < 다른 풀이 >
    # Counter : 딕셔너리의 데이터의 개수를 계산해주는 라이브러리
    # reduce : 반복 가능한 객체(iterable object)(ex : list, dictionary) 내 각 요소를 연산한 뒤 이전 연산 결과들과 누적해서 반환해 주는 함수
      reduce(function, iterable, initializer=None) -> function : 함수, iterable : 반복하는 객체, initializer : 시작값(Value placed before the iterable)
    
    def solution(clothes):
        from collections import Counter
        from functools import reduce
        cnt = Counter([kind for name, kind in clothes])
        answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
        return answer
'''