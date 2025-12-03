import os 
path = os.getcwd() + "\\Day1\\source.txt"
f = open(path, "r")

currentDialPos = 50
result = 0

def turnDial(turnType, turnAmountStr):
    global currentDialPos
    turnAmount = int(turnAmountStr)
    if turnType == "L":
        turnAmount = -turnAmount
    
    currentDialPos += turnAmount
    currentDialPos = currentDialPos % 100

for turn in f:
    turn.strip()
    print("Turning:"+turn)
    turnDial(turn[0], turn[1:])
    
    #print(currentDialPos)
    if currentDialPos == 0:
        result += 1

print("Result: "+str(result))

f.close()