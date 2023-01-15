# 코딩테스트 연습 / 깊이/너비 우선 탐색(DFS/BFS) / 네트워크

def solution(n, computers):
    network = []

    for i in range(n):
        for j in range(i+1):
            if computers[i][j] == 1:
                if not network:
                    network.append(set([i, j]))
                else:
                    node = set([i, j])
                    for idx, n in enumerate(network):
                        if node & n:
                            network[idx] = network[idx].union(node)
                            break
                    else:
                        network.append(node)

    return len(network)


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
