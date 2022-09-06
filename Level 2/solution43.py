# 코딩테스트 연습 / Summer/Winter Coding(~2018) / 스킬트리
# 문자열에서 해당 문자의 인덱스를 찾고 오름차순인지 확인

def solution(skill, skill_trees):
    count = 0
    for skill_tree in skill_trees:
        s = ""                      # 하나의 스킬트리를 뽑을 때마다 s 초기화
        for ch in skill_tree:       
            if ch in skill:         # 스킬트리 중에 skill이 있다면 s에 추가
                s += ch
        
        if skill[:len(s)] == s:     # 만든 s를 기준으로 skill과 같다면 count += 1
            count += 1
    
    return count

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))           # 2

'''
    < 다른 풀이 >
    # for-else 문의 경우 for문이 정상적으로 실행된다면 else 문의 결과가 실행되도록 구성
    def solution(skill, skill_trees):
        answer = 0

        for skills in skill_trees:
            skill_list = list(skill)

            for s in skills:
                if s in skill:
                    if s != skill_list.pop(0):
                        break
            else:
                answer += 1

        return answer
'''