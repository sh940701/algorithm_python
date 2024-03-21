class Stack:
    def __init__(self):
        self.arr = []

    def push(self, num):
        return self.arr.append(num)

    def pop(self):
        if len(self.arr):
            value = self.arr[-1]
            self.arr = self.arr[:-1]
            return value
        else:
            return -1

    def size(self):
        return len(self.arr)

    def empty(self):
        return 1 if len(self.arr) == 0 else 0

    def top(self):
        return self.arr[-1] if len(self.arr) else -1

    @staticmethod
    def static(num):
        print(num)


N = int(input())
arr = [list(input().split()) for _ in range(N)]

stack = Stack()

Stack.static

for item in arr:
    if item[0] == 'push':
        stack.push(item[1])

    elif item[0] == 'top':
        print(stack.top())

    elif item[0] == 'size':
        print(stack.size())

    elif item[0] == 'empty':
        print(stack.empty())

    elif item[0] == 'pop':
        print(stack.pop())
