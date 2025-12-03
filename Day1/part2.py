import os 
path = os.getcwd() + "\\Day1\\source.txt"
f = open(path, "r")

currentDialPos = 50
result = 0

def turnDial(turnAmount):
    global currentDialPos

    currentDialPos += turnAmount
    currentDialPos = currentDialPos % 100
    
def repeatTurnDial(turnType, turnAmountStr):
    global result
    global currentDialPos
    
    turnAmount = int(turnAmountStr)
    turnCount = 1
    if turnType == "L":
        turnCount = -1
    
    for _ in range(0, turnAmount):
        turnDial(turnCount)
        if currentDialPos == 0:
            result += 1

for turn in f:
    turn.strip()
    print("Turning:"+turn)
    repeatTurnDial(turn[0], turn[1:])

print("Result: "+str(result))

f.close()