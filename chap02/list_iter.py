x = ['John', 'George', 'Paul', 'Ringo']

result = iter(x)
for i in range(len(x)):
    print(result.__next__())
