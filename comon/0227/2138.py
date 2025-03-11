n = int(input())
bulb = list(map(int, input()))
target = list(map(int, input()))


def change(A, B):
    A_copy = A[:]
    press = 0
    for i in range(1, n):

        if A_copy[i-1] == B[i-1]:
            continue

        press += 1
        for j in range(i-1, i+2):
            if j < n:
                A_copy[j] = 1 - A_copy[j]
    if A_copy == B:
        return press
    else:
        return 1e9


res = change(bulb, target)
# 첫번째 전구의 스위치를 누르는 경우
bulb[0] = 1 - bulb[0]
bulb[1] = 1 - bulb[1]
# 비교
res = min(res, change(bulb, target) + 1)  # min(첫번째 전구x, 첫번째 전구 o)
if res != 1e9:
    print(res)
else:
    print(-1)

# n = int(input())

# start = list(map(int, list(input())))
# target = list(map(int, list(input())))

# queue = [(start, 0)]

# is_find = False

# while (queue and (not is_find)):
#     new_case, count = queue.pop(0)
#     if new_case == target:
#         print(count)
#         break

#     for i in range(len(new_case)):
#         next_case = new_case[::]
#         if i == 0:    # 처음인 경우
#             next_case[0] = (next_case[0]+1) % 2
#             next_case[1] = (next_case[1]+1) % 2
#         elif i == n-1:    # 마지막인 경우
#             next_case[-1] = (next_case[-1]+1) % 2
#             next_case[-2] = (next_case[-2]+1) % 2
#         else:    # 일반 케이스
#             next_case[i-1] = (next_case[i-1]+1) % 2
#             next_case[i] = (next_case[i]+1) % 2
#             next_case[i+1] = (next_case[i+1]+1) % 2

#         if next_case == target:
#             print(count+1)
#             is_find = True
#         else:
#             queue.append((next_case, count+1))

# if not is_find:
#     print(-1)
