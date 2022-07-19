# 코딩테스트 연습 / 2020 KAKAO BLIND RECRUITMENT / 문자열 압축

def solution(s):
    result=[]
    
    # 길이가 1이면 무조건 최솟값이다
    if len(s)==1:
        return 1
    
    for i in range(1, len(s)+1):
        b = ''
        cnt = 1
        tmp=s[:i]

        # 처음 텍스트를 자르고 자른 길이만큼 문자열을 잘라내 확인하며 같은지 확인
        # 마지막 문자열도 확인해야 하므로 길이를 len(s) + i로 계산
        # 최대 길이는 문자열 길이의 반 -> len(s)/2
        for j in range(i, len(s)+i, i):
            # 같은 문자열이 있다면 계속 진행
            if tmp==s[j:i+j]:
                cnt+=1
            else:
                # 이제 다른 문자가 나오면 이전 문자까지 읽을 것을 확인하고, 1이 아닌경우 해당 개수를 1인 경우는 아무것도 적지 않는다
                if cnt!=1:
                    b = b + str(cnt)+tmp
                else:
                    b = b + tmp
                    
                tmp=s[j:j+i]
                cnt = 1
                
        # 일단 모아놓고 한번에 비교하여 출력
        result.append(len(b))

    return min(result)

print(solution("aabbaccc")) #7
print(solution("ababcdcdababcdcd"))	#9
print(solution("abcabcdede"))	#8
print(solution("abcabcabcabcdededededede"))	#14
print(solution("xababcdcdababcdcd"))    #17