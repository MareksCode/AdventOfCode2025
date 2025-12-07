import os 
path = os.getcwd() + "\\Day6\\source.txt"
f = open(path, "r")

numbers = []
for line in f:
    numbers.insert(len(numbers), line.strip().split())

finalResult = 0
for x in range(0, len(numbers[0])):
    operation = numbers[len(numbers)-1][x]
    
    def use(num1, num2):
        result = -1
        if operation == "+":
            result = num1+num2
        if operation == "*":
            result = num1*num2

        return result
    
    currentResult = 0
    if operation == "*":
        currentResult = 1
    
    for numY in range(0, len(numbers)-1):
        num = numbers[numY][x]
        currentResult = use(currentResult, int(num))
    
    finalResult+= currentResult
print(finalResult)

f.close()