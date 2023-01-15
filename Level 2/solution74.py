# 코딩테스트 연습 / 연습문제 / N-Queen
# 백트래킹을 이용하는 전형적인 N-Quenn 문제

def solution(n):
    def comp(x, y, col):
        for i in range(x):
            if y == col[i] or (abs(y-col[i]) == abs(x-i)):
                return False
        else:
            return True

    def nQueen(x, n, cols):
        if x == n:
            return 1

        count = 0
        for col in range(n):
            if comp(x, col, cols):
                cols[x] = col
                count += nQueen(x+1, n, cols)

        return count

    # main
    cols = [0]*n
    answer = nQueen(0, n, cols)

    return answer


print(solution(4))      # 2
