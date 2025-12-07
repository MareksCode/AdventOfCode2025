import os 
path = os.getcwd() + "\\Day5\\testSourceIDs.txt"
f1 = open(path, "r")

path2 = os.getcwd() + "\\Day5\\testSourceRanges.txt"
f2 = open(path2, "r")

l = []
for x in f2:
    l.insert(len(l), x.split("-"))

f2.close()

result = 0
for x in f1:
    isFresh = False
    newId = int(x)
    
    for rng in l:
        if newId >= int(rng[0]) and newId <= int(rng[1]):
            #print("is fresh: "+x+" / "+rng[0]+" / "+rng[1])
            isFresh = True
    
    if isFresh:
        result+=1

print(result)

f1.close()