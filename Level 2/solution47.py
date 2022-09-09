# 코딩테스트 연습 / Summer/Winter Coding(~2018) / 영어 끝말잇기
# 문자열 문제 / for-else 문을 통해 작업이 끝까지 수행되면 종료

def solution(n, words):
    turns = 0

    wordList = []   
    lastWord = ""
    for word in words:
        # 초기값
        if lastWord == "":
            wordList.append(word)
            lastWord = word
        
        # 만약 끝말잇기가 안된다면
        elif lastWord[-1] != word[0]:
            turns += 1
            break
    
        # 만약 중복된 단어가 나온다면
        elif word in wordList:
            turns += 1
            break
        
        turns += 1
        wordList.append(word)
        lastWord = word
    
    else:
        return [0,0]
    
    cycle = 1
    while turns > n:
        turns -= n
        cycle += 1
    
    return [turns, cycle]

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))      # [3,3]
print(solution(5,["hello", "observe", "effect", "take", "either", "recognize",
                  "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]	))      # [0,0]
print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))      # [1,3]


'''
    < 다른 풀이 >
    # 나머지 연산을 통해 해당 단어를 확인 할 수 있음
    
    def solution(n, words):
        for p in range(1, len(words)):
            if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
        else:
            return [0,0]
'''