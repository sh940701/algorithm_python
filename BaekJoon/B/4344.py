N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for scores in arr:
    score_count = scores[0]
    mean = sum(scores[1:]) / score_count

    over_avg_count = 0

    for score in scores[1:]:
        if score > mean:
            over_avg_count += 1

    print(f'{round(over_avg_count / score_count * 100, 3)}%')
