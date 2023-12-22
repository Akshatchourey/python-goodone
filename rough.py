import re

n = int(input())
def helper(str):
    dot = idx = 0
    if str[0] == '+' or str[0] == '-':
        idx += 1
    if str[0] == '.':
        idx += 1
        dot += 1

    for i in range(idx, len(str)):
        if dot == 1:
            if not(re.match(r"\d", str[i])):
                print("False")
                return
            dot += 1
            continue
        if str[i] == '.':
            dot += 1
        if not(re.match(r"\d", str[i])) and dot != 1:
            print("False")
            return
    if dot < 1:
        print("False")
    else:
        print("True")


for j in range(n):
    helper(str(input()))

