# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# print(arr)
#
# result = []
#
# num = 329
# hint_count = 0
#
# for hint in arr:
#     question = hint[0]
#     strike_count = 0
#     ball_count = 0
#
#     for i, s in enumerate(str(question)):
#         if s in str(num):
#             if str(question)[i] == str(num)[i]:
#                 strike_count += 1
#             else:
#                 ball_count += 1
#
#     if strike_count == hint[1] and ball_count == hint[2]:
#         hint_count += 1
#
# if hint_count == N:
#     result.append(num)
#
# print(result)


# for i in range(1, 10):
#     for j in range(10):
#         for k in range(10):
#             if i == j or j == k or k == i:
#                 continue
#
#             print(i, j, k)
#
#             num = i * 100 + j * 10 + k
#
#             print(num)
#
#             hint_count = 0
#
#             for hint in arr:
#                 question = hint[0]
#                 strike_count = 0
#                 ball_count = 0
#
#                 for i, s in enumerate(str(question)):
#                     if s in str(num):
#                         if str(question)[i] == str(num)[i]:
#                             strike_count += 1
#                         else:
#                             ball_count += 1
#
#                 if strike_count == hint[1] and ball_count == hint[2]:
#                     hint_count += 1
#
#             if hint_count == N:
#                 result.append(num)
#
#
# print(result)


def recur(hint_idx, number):
    if hint_idx == N:
        answer += 1
        recur(0, number + 1)
        return

    if number == 1000:
        return

    # 만약에 힌트에 통과했다면
    recur(hint_idx + 1, number)

    # 만약에 힌트에 통과하지 않았다면
    recur(0, number + 1)


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0

recur(0, 100)
