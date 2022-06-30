# 코딩테스트 연습 / 정렬 / K번째수

def solution(array, commands):
    answer = []
    
    for case in commands:
        tmp = array[case[0]-1:case[1]]
        tmp.sort()
        answer.append(tmp[case[2]-1])
    
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

'''
< 다른 풀이 >
map은 리스트의 요소를 지정된 타입 or 함수로 처리해주는 함수 -> list(map(형식, 대상)) : list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
sorted(리스트) -> 정렬된 리스트를 리턴
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
'''