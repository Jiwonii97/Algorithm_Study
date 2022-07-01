# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [1차] 비밀지도

def solution(n, arr1, arr2):
    answer = []
    for n1, n2 in zip(arr1,arr2):
        tmp = bin(n1|n2)[2:].replace("1","#").replace("0"," ").rjust(n," ")
        answer.append(tmp)
        
    return answer

'''
    < 다른 풀이 >
    # bin으로 수를 이진법으로 바꾸고 rjust로 특정한 문자열 길이를 맞춤
    # replace로 문자열 교체
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
'''