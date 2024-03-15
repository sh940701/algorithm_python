x, y, w, h = map(int, input().split())

result_x = 0
result_y = 0

result_x = x if (w / 2) > x else w - x
result_y = y if (h / 2) > y else h - y

print(min(result_x, result_y))
