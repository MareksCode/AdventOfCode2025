import os

path2 = os.getcwd() + "\\Day5\\testSourceRanges.txt"
f2 = open(path2, "r")

l = []
for x in f2:
    parts = x.split("-")
    num1 = int(parts[0])
    num2 = int(parts[1])
    l.append((num1, num2))

l.sort()

l2 = []
curStart = l[0][0]
curEnd = l[0][1]

for rng in l[1:]:
    print("adding rng: " + str(rng))
    start = rng[0]
    end = rng[1]

    if start <= curEnd + 1:
        curEnd = max(curEnd, end)
    else:
        l2.append((curStart, curEnd))
        curStart = start
        curEnd = end

    print("added rng: " + str(rng))

l2.append((curStart, curEnd))

count = 0
for rng in l2:
    count += (rng[1] - rng[0] + 1)

print(count)

f2.close()