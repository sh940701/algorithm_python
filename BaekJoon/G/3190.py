from collections import deque

N = int(input())
A = int(input())
apples = set(tuple(map(int, input().split())) for _ in range(A))

L = int(input())
change_direction_time = dict()

for _ in range(L):
    direction = list(input().split())
    change_direction_time[int(direction[0])] = direction[1]

directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']

snake = deque()
snake.append((1, 1))

result = None

count = 0

current_direction = 'RIGHT'
while True:
    count += 1
    if current_direction == 'RIGHT':
        next_target = (snake[0][0], snake[0][1] + 1)
        snake.appendleft(next_target)
        if snake[0][0] == N + 1 or snake[0][0] == 0 or snake[0][1] == N + 1 or snake[0][1] == 0 or snake.count(
                snake[0]) == 2:
            result = count
            break

        elif next_target in apples:
            apples.remove(next_target)
        else:
            snake.pop()

    elif current_direction == 'LEFT':
        next_target = (snake[0][0], snake[0][1] - 1)
        snake.appendleft(next_target)
        if snake[0][0] == N + 1 or snake[0][0] == 0 or snake[0][1] == N + 1 or snake[0][1] == 0 or snake.count(
                snake[0]) == 2:
            result = count
            break

        elif next_target in apples:
            apples.remove(next_target)
        else:
            snake.pop()

    elif current_direction == 'UP':
        next_target = (snake[0][0] - 1, snake[0][1])
        snake.appendleft(next_target)
        if snake[0][0] == N + 1 or snake[0][0] == 0 or snake[0][1] == N + 1 or snake[0][1] == 0 or snake.count(
                snake[0]) == 2:
            result = count
            break

        elif next_target in apples:
            apples.remove(next_target)
        else:
            snake.pop()

    elif current_direction == 'DOWN':
        next_target = (snake[0][0] + 1, snake[0][1])
        snake.appendleft(next_target)
        if snake[0][0] == N + 1 or snake[0][0] == 0 or snake[0][1] == N + 1 or snake[0][1] == 0 or snake.count(
                snake[0]) == 2:
            result = count
            break

        elif next_target in apples:
            apples.remove(next_target)
        else:
            snake.pop()

    if change_direction_time.get(count):
        if current_direction == 'UP':
            if change_direction_time.get(count) == 'D':
                current_direction = 'RIGHT'
            else:
                current_direction = 'LEFT'

        elif current_direction == 'DOWN':
            if change_direction_time.get(count) == 'D':
                current_direction = 'LEFT'
            else:
                current_direction = 'RIGHT'

        elif current_direction == 'RIGHT':
            if change_direction_time.get(count) == 'D':
                current_direction = 'DOWN'
            else:
                current_direction = 'UP'

        elif current_direction == 'LEFT':
            if change_direction_time.get(count) == 'D':
                current_direction = 'UP'
            else:
                current_direction = 'DOWN'

print(result)
