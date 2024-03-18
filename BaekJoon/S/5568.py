# N 개 중에 K 개를 뽑는다. -> 이 때 하나를 뽑아서 어디에 놓는지 순서가 필요하기 때문에, 순열 알고리즘을 사용해야 한다.
# https://yangnyang.tistory.com/m/14

N = int(input())
T = int(input())

arr = list(int(input()) for _ in range(N))


# 순열 구하기 알고리즘
def permutation(arr, n):
    result = []

    # 하나의 배열에서 그보다 더 많은 요소를 고를 수 없기 때문에 예외처리
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])

    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]  # ans == [1, 2, 3]
            ans.remove(arr[i])  # ans == [2, 3], [1, 3], [1, 2]
            for p in permutation(ans, n - 1):
                result.append([arr[i]] + p)

    return result


result = set()

for item in permutation(arr, T):
    result.add(''.join(map(str, item)))

print(len(result))
