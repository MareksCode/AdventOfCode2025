import os 
path = os.getcwd() + "\\Day3\\source.txt"
f = open(path, "r")

endResult = 0
for bankString in f:
    biggestNum = -1
    biggestXIndex = -1
    for x in range(len(bankString)-2):
        numAtX = int(bankString[x])
        if numAtX > biggestNum:
            biggestNum = numAtX
            biggestXIndex = x
    
    secondBiggestNum = -1
    for x in range(biggestXIndex+1, len(bankString)-1):
        numAtX = int(bankString[x])
        if numAtX > secondBiggestNum:
            secondBiggestNum = numAtX

    biggestNum*=10
    endResult += biggestNum + secondBiggestNum

print(endResult)

f.close()