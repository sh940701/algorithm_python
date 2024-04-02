from collections import defaultdict, deque

N, K = list(map(int, input().split()))
arr = list(map(int, input().split()))

plugs = set()

count = 0

while len(plugs) < N and count < K:
    plugs.add(arr[count])
    count += 1

mapping = defaultdict(deque)

answer = 0

# 모든 수가 각각 몇번째 순서로 등장하는지 저장
for idx in range(count, K):
    mapping[arr[idx]].append(idx)

for idx in range(count, K):
    maximum_idx = float('-inf')
    maximum_idx_item = None
    if arr[idx] in plugs:
        if mapping[arr[idx]]:
            mapping[arr[idx]].popleft()
        continue


    for item in plugs:

        if not mapping[item]:
            plugs.remove(item)
            plugs.add(arr[idx])
            if mapping[arr[idx]]:
                mapping[arr[idx]].popleft()
            answer += 1
            break
        if mapping[item][0] > maximum_idx:
            maximum_idx = mapping[item][0]
            maximum_idx_item = item
    else:
        plugs.remove(maximum_idx_item)
        plugs.add(arr[idx])
        if mapping[arr[idx]]:
            mapping[arr[idx]].popleft()
        answer += 1

print(answer)
