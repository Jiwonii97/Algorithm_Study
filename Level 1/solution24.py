# 코딩테스트 연습 / 월간 코드 챌린지 시즌3 / 나머지가 1이 되는 수 찾기
# 나머지가 1인 수를 찾으면 되므로 1을 뺐을때 나눠지는 수를 찾으면 됨

def solution(n):
    return list(x for x in range(2,n+1) if (n-1) % x == 0)[0]