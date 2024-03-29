import sys

text = sys.stdin.readline().strip()

new = ""
num = ""
minus_flag = 0

for t in text:
    if '0' <= t <= '9':
        num += t
    elif t == '-':
        new += str(int(num))
        num = ""
        if minus_flag == 0:
            new += t
            new += "("
            minus_flag = 1
        else:
            new += ")" + t + "("
    else:
        new += str(int(num)) + t
        num = ""

new += str(int(num))
if minus_flag:
    new += ")"

print(eval(new))
