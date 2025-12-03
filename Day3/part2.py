import os 
path = os.getcwd() + "\\Day3\\source.txt"
f = open(path, "r")

def getBiggestNumAndXInRange(startXIndex, bankString, endXIndex):
    biggestNum = -1
    biggestX = -1
    for x in range(startXIndex, endXIndex + 1):
        numAtX = int(bankString[x])
        if numAtX > biggestNum:
            biggestNum = numAtX
            biggestX = x
    return biggestNum, biggestX

endResult = 0
for bankString in f:
    bankString = bankString.strip()
    
    print("Bank string:"+bankString)
    lastXIndex = 0
    totalNumber = 0
    for mult in range(12,0,-1):
        biggestNum, biggestX = getBiggestNumAndXInRange(lastXIndex, bankString, len(bankString)-mult)
        totalNumber += biggestNum * 10**(mult-1)
        lastXIndex = biggestX + 1
        print(str(lastXIndex)+" - "+str(totalNumber)+" @ "+str(mult))
    print("Total number: ------- "+str(totalNumber))
    
    endResult+= totalNumber
    print("end result: "+str(endResult))

print("final end Result:"+str(endResult))

f.close()