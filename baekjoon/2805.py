N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)  # 이분탐색 범위 설정

while start <= end:  # 적절한 벌목 높이를 찾는 알고리즘
    mid = (start+end) // 2

    cut_tree = 0  # 벌목된 나무 총합
    for i in tree:
        cut_tree += max(0, i-mid)

    # 벌목 높이를 이분탐색
    if cut_tree >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
