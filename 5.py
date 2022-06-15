# 코딩테스트 연습 / 2021 카카오 채용연계형 인턴십 / 숫자 문자열과 영단어
# 정석 풀이!! ( 딕셔너리 활용 )

def solution(s):    
    _num = {"zero":0, "one":1, "two":2, "three" : 3, "four":4,
            "five":5, "six":6, "seven":7, "eight" : 8, "nine":9}
    
    for key, value in _num.items():
        if key in s:
            s = s.replace(key,str(value))
    
    return int(s)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))