import os 
path = os.getcwd() + "\\Day2\\source.txt"
f = open(path, "r")

fullString = f.read()
splitIds = fullString.split(",")

allInvalidIds = 0

def isValid(number):
    strNum = str(number)
    if len(strNum)%2!=0:
        return True
    
    middle = int(len(strNum)/2)
    for x in range(0,middle):
        if strNum[x] != strNum[x+middle]:
            return True
    
    return False
        
for idStr in splitIds:
    innerIds = idStr.split("-")
    
    rangeStart = innerIds[0]
    rangeEnd = innerIds[1]
    
    print("------ Range: "+rangeStart+" to "+rangeEnd+" ------")
    
    if rangeStart[0] == "0" or rangeEnd[0] == "0":
        print("leading 0! Continuing")
        continue
    for x in range(int(rangeStart), int(rangeEnd)+1):
        #print(str(x)+" is valid: "+str(isValid(x)))
        if not isValid(x):
            allInvalidIds += x

print("All added up: "+str(allInvalidIds))

f.close()