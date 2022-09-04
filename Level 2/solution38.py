# 코딩테스트 연습 / 2019 카카오 개발자 겨울 인턴십 / 튜플

def solution(s):
    answer = []
       
    _list = sorted(eval(s.replace("{","[").replace("}","]")),key=lambda x: len(x))
    for s in _list:
        tmp = set(s) - set(answer)
        answer.extend(tmp)
    
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))      # [2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))      # [2, 1, 3, 4]
print(solution("{{20,111},{111}}"))      # [111, 20]
print(solution("{{123}}"))     # [123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))     # [3, 2, 4, 1]


''' 
    < 다른 풀이 >

    def solution(s):
        answer = []

        # lstrip, rstrip을 통해 좌우의 괄호를 제거하고 파싱 진행
        s1 = s.lstrip('{').rstrip('}').split('},{')

        new_s = []
        for i in s1:
            new_s.append(i.split(','))

        # 원소가 들어가면 리스트의 길이가 무조건 커지므로 길이순으로 정렬하여 하나씩 걸러냄
        new_s.sort(key = len)

        for i in new_s:
            for j in range(len(i)):
                if int(i[j]) not in answer:
                    answer.append(int(i[j]))

        return answer
    
    # 내 방식과 매우 유사하지만 list compreprehension을 사용하여 좀더 pythonic 함
    def solution(s):
        s = eval(s.replace("{", "[").replace("}", "]"))
        answer = list({num:0 for k in sorted(s, key=lambda x: len(x)) for num in k}.keys())
        return answer
    
'''