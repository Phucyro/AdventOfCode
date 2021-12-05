def parseFile(inputFile):
    listOfValues = []
    for line in inputFile:
        strippedLine = line.strip()
        lineList = strippedLine.split()
        listOfValues.append(lineList)
    return listOfValues

def getFinalCoordinates(listOfValues):
    
    horizontalPosition = 0
    depth = 0
    aim = 0
    
    for valueCouple in listOfValues:
        
        instruction = valueCouple[0]
        units = int(valueCouple[1])
        
        if (instruction == 'forward'):
            horizontalPosition += units
            depth += aim * units
        
        elif (instruction == 'down'):
            
            aim += units
            
        elif (instruction == 'up'):
            
            aim -= units
    
    print("Horizontal position: " + str(horizontalPosition))
    print("Depth: " + str(depth))
    return(horizontalPosition, depth)
            
        

def main():
       
    try:       
        inputFile = open("C:/Users/phucy/Desktop/AdventOfCode/Day2/input.txt","r")
        listOfValues = parseFile(inputFile)
        getFinalCoordinates(listOfValues)
               
    except:
        print('error opening file')
    
    
if __name__ == '__main__':
    main()