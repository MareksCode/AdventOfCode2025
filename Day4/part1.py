import os 
path = os.getcwd() + "\\Day4\\source.txt"
f = open(path, "r")

lineCount = 0
lineLength = 0

patternArray = [[-1,-1],[1,-1],[-1,1],[1,1],[0,-1],[0,1],[-1,0],[1,0]]

for line in f:
    lineCount+=1
    if lineCount == 1:
        for x in line.strip():
            lineLength+=1

f.seek(0)

field = [[None for _ in range(lineCount)] for _ in range(lineLength)]

currentLine = -1
currentColumn = -1
for line in f:
    currentLine+=1
    strippedLine = line.strip()
    for roll in strippedLine:
        currentColumn+=1
        if roll == "@":
            field[currentLine][currentColumn] = True
        else:
            field[currentLine][currentColumn] = False
    currentColumn = -1

def fieldHasSomethingAtPattern(pattern, midX, midY):
    x = pattern[0] + midX
    y = pattern[1] + midY
    
    if x < 0 or y < 0:
        return False
    if x >= lineCount or y >= lineLength:
        return False
    
    return field[x][y]

def check(x,y):
    global patternArray
    foundRolls = 0
    for pattern in patternArray:
        #print("Checking Pattern: "+str(pattern)+" - "+str(fieldHasSomethingAtPattern(pattern,x,y)))
        if fieldHasSomethingAtPattern(pattern, x, y):
            foundRolls+=1
    
    return foundRolls < 4

#print(field)

result = 0
for x in range(0,len(field)):
    for y in range(0, len(field[0])):
        if field[x][y] == False:
            continue
        
        #print("checking: "+str(field[x][y]))
        if check(x,y):
            print(str(x)+" ; "+str(y))
            result+=1
print(result)
f.close()