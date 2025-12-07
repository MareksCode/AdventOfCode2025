import os
path = os.getcwd() + "\\Day6\\source.txt"
f = open(path, "r")

lines = [l.rstrip("\n").replace("\t", "    ") for l in f]

maxlen = max(len(l) for l in lines)
for i in range(len(lines)):
    lines[i] = lines[i].ljust(maxlen)

h = len(lines)
last = h - 1
finalResult = 0
x = maxlen - 1

while x >= 0:
    colEmpty = True
    for y in range(h):
        if lines[y][x] != " ":
            colEmpty = False
            break
    if colEmpty:
        x -= 1
        continue

    cols = []
    while x >= 0:
        empty = True
        for y in range(h):
            if lines[y][x] != " ":
                empty = False
                break
        if empty:
            break
        cols.append(x)
        x -= 1

    cols = cols[::-1]

    operation = None
    for c in cols:
        if lines[last][c] in ("+", "*"):
            operation = lines[last][c]
            break

    if operation is None:
        continue

    def use(a, b):
        if operation == "+":
            return a + b
        if operation == "*":
            return a * b
        return 0

    values = []
    for col in cols:
        numStr = ""
        for row in range(h - 1):
            c = lines[row][col]
            if c.isdigit():
                numStr += c
        if numStr == "":
            number = 0
        else:
            number = int(numStr)
        values.append(number)

    if operation == "+":
        current = 0
    else:
        current = 1

    for v in values:
        current = use(current, v)

    finalResult += current

print(finalResult)
