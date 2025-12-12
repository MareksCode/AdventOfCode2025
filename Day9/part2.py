import os 
path = os.getcwd() + "\\Day9\\source.txt"
f = open(path, "r")

coordsAsString = []
for line in f:
    coordsAsString.append(line.strip().split(","))

coords = []
for stringCoordArr in coordsAsString:
    coords.append([int(stringCoordArr[0]),int(stringCoordArr[1])])

def getArea(coord1, coord2):
    x1 = abs(coord1[0] - coord2[0])+1
    x2 = abs(coord1[1] - coord2[1])+1
    
    return x1*x2

largestArea = -1

for coord in coords:
    for otherCoord in coords:
        if getArea(coord, otherCoord) > largestArea:
            print(str(coord)+" / "+str(otherCoord))
            largestArea = getArea(coord, otherCoord)

print(largestArea)

f.close()