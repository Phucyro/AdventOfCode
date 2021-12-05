def getDepthMeasurementIncrease(inputFile):
    
    numberOfIncrease = 0
    
    listOfValues = parseFile(inputFile)
    
    for x in range(1,len(listOfValues)):
        if listOfValues[x] > listOfValues[x-1]:
            numberOfIncrease += 1
            
    print("Number of increases: " + str(numberOfIncrease))
    
    return numberOfIncrease

def parseFile(inputFile):
    listOfValues = []
    
    for line in inputFile:
        strippedLine = line.strip()
        listOfValues.append(int(strippedLine))
    
    return listOfValues

def main():
       
    try:       
        inputFile = open("C:/Users/phucy/Desktop/AdventOfCode/Challenge1/input.txt","r")
                  
    except:
        print('error opening file')
        
    getDepthMeasurementIncrease(inputFile)
    
       
if __name__ == '__main__':
    main()
