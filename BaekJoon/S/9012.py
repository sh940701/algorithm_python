N = int(input())
vpc_list = list(input() for _ in range(N))

for idx, string in enumerate(vpc_list):
    arr = []

    for vps in string:
        if vps == '(':
            arr.append(1)
        else:
            if not len(arr):
                print('NO')
                break
            else:
                arr.pop()
    else:
        print('YES') if len(arr) == 0 else print('NO')
