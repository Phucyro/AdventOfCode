import copy

def parseFile(inputFile):
    listOfValues = []
    
    for line in inputFile:
        strippedLine = line.strip()
        listOfValues.append(strippedLine)
    
    return listOfValues

def getValueCountList(values,binaryNumberCount, binaryNumberLength):
    
    valueCountPerPosition = []
    
    for x in range(binaryNumberLength):
 
        choicesCount = [0,0]
        valueCountPerPosition.append(choicesCount)
    
    """ Loop one binary number to another and add to the count
    """
    for number in range(binaryNumberCount):
        for position in range(binaryNumberLength):   
            value = int(values[number][position])
            
            if value == 0:
                valueCountPerPosition[position][0] += 1
        
            elif value == 1:
                valueCountPerPosition[position][1] += 1
    
    return valueCountPerPosition



def getRates(values):
    
    binaryNumberLength = len(values[0])
    binaryNumberCount = len(values)
    
    """ GET list of count per column
        ((count of 0 position 0, count Of 1 position 0)(...)(...))
    """
    
    valueCountPerPosition = getValueCountList(values,binaryNumberCount, binaryNumberLength)
    
    """ Get gamma and epsilon rate
    if most common 1 -> gamma rate = 1, epsilon rate = 0
    if most common 0 -> gamme rate = 0, epsilon rate = 1
    """
    
    gammaRate = ""
    epsilonRate = ""
        
    for position in range(binaryNumberLength):
        
        countOfZeros =  valueCountPerPosition[position][0]
        countOfOnes = valueCountPerPosition[position][1]

        
        if countOfOnes > countOfZeros:
           gammaRate += "1"
           epsilonRate += "0"
        
        elif countOfZeros > countOfOnes:
           gammaRate += "0"
           epsilonRate += "1"
        
    
    print("Gamma rate: " + gammaRate)
    print("Epsilon rate: " + epsilonRate)
    
def verifyLifeSupportRating(values):
    
    binaryNumberLength = len(values[0])
    binaryNumberCount = len(values)

    
    """get oxygen generator rating and CO2 scrubber rating
    """
    
    """get oxygen generator
    """
    
    copyOfValues = copy.deepcopy(values)
    
    
    finished = False
    currentPosition = 0
    
    
    while (not finished):
        
        if len(copyOfValues) == 1:
            finished = True
        
        else:
            valueCountPerPosition = getValueCountList(copyOfValues,len(copyOfValues), binaryNumberLength)
            
            currentChoiceCount = valueCountPerPosition[currentPosition]
            
            countOfZeros = int(currentChoiceCount[0])
            countOfOnes = int(currentChoiceCount[1])
            
            if (countOfOnes > countOfZeros) or (countOfZeros == countOfOnes):
                #delete all the numbers who have 0 in that position
                
                toDeletePosition = []
                
                for number in range(len(copyOfValues)):
                    
                    if (int(copyOfValues[number][currentPosition])) != 1:
                        toDeletePosition.append(number)
                
                #delete
                for index in reversed(toDeletePosition):
                    del copyOfValues[index]
                
                    
                    
            elif (countOfZeros > countOfOnes):
                #delete all the numbers who have 1 in that position
                toDeletePosition = []
                
                for number in range(len(copyOfValues)):
                    
                    
                    if int(copyOfValues[number][currentPosition]) != 0:
                        toDeletePosition.append(number)
                        
                #delete
                for index in reversed(toDeletePosition):
                    del copyOfValues[index]
            
            currentPosition+=1
            
    oxygenGeneratorRating = copyOfValues[0]
    print("oxygen generator rating : " + oxygenGeneratorRating)
    

    """get CO2 scrubber rating
    """
    
    copyOfValues = copy.deepcopy(values)
    
    
    finished = False
    currentPosition = 0
    
    while (not finished):
        
        if len(copyOfValues) == 1:
            finished = True
        
        else:
            
            valueCountPerPosition = getValueCountList(copyOfValues,len(copyOfValues), binaryNumberLength)
            
            currentChoiceCount = valueCountPerPosition[currentPosition]
            
            countOfZeros = int(currentChoiceCount[0])
            countOfOnes = int(currentChoiceCount[1])
            
            
            if (countOfZeros < countOfOnes) or (countOfZeros == countOfOnes):
                #on delete tous les 1
                toDeletePosition = []
                
                for number in range(len(copyOfValues)):
                    
                    if (int(copyOfValues[number][currentPosition]) != 0):
                        toDeletePosition.append(number)
                
                for index in reversed(toDeletePosition):
                    
                    del copyOfValues[index]
            
            elif (countOfOnes < countOfZeros):
                
                toDeletePosition = []
                
                for number in range(len(copyOfValues)):
                    
                    if (int(copyOfValues[number][currentPosition]) != 1):
                        toDeletePosition.append(number)
                
                for index in reversed(toDeletePosition):
                    
                    del copyOfValues[index]
            
            currentPosition += 1
    
    scrubberRating = copyOfValues[0]
    print("scrubber rating : " + scrubberRating)
                    
    
    
    
def main():
       
    try:       
        inputFile = open("C:/Users/phucy/Desktop/AdventOfCode/Day3/input.txt","r")
        foundValues = parseFile(inputFile)
        getRates(foundValues)
        verifyLifeSupportRating(foundValues)       
    except:
        print('error opening file')
        
    
    
    
       
if __name__ == '__main__':
    main()