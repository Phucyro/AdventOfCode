def getSlidingWindowMeasurement(listOfValues):
    
    numberOfIncrease = 0
           
    for x in range(0,len(listOfValues)-3):
        
        firstSum = listOfValues[x] + listOfValues[x+1] + listOfValues[x+2]
        secondSum = listOfValues[x+1] + listOfValues[x+2] + listOfValues[x+3]
        
        if secondSum > firstSum:
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
    
    listOfValues = parseFile(inputFile)
    getSlidingWindowMeasurement(listOfValues)
    
       
if __name__ == '__main__':
    main()