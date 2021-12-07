def parseFile(inputFile):
    
    listOfValues = inputFile.read().split(",")
    listOfValues = [int(x) for x in listOfValues]
    
    return listOfValues

def getLanternFishSizeSimulationRecursive(lanternFishList, numberOfDays):
    """Nice try but not optimized
    """
      
    if (numberOfDays == 0):
        
        print("It is all over")
        print(len(lanternFishList))
        
    else:
        
        newFishCount = 0
        
        for fishNumber in range(len(lanternFishList)):
            
            if lanternFishList[fishNumber] == 0:
                #produce new fish
                lanternFishList[fishNumber] = 6
                newFishCount += 1
            else:
                lanternFishList[fishNumber] -= 1
            
        for i in range(newFishCount):
            lanternFishList.append(8)
        
        numberOfDays -= 1
        
        getLanternFishSizeSimulationRecursive(lanternFishList, numberOfDays)
    
def getCountList(lanternFishList):
    
    result = [0 for i in range(9)]
    
    for fishNumber in range(len(lanternFishList)):
        daysLeftValue = lanternFishList[fishNumber]
        result[daysLeftValue] += 1
    
    return result
        
              
def getLanternFishSizeSimulation(lanternFishList, numberOfDays):
    
    countList = getCountList(lanternFishList)
    countListSize = len(countList)
    
    for daysLeft in range(numberOfDays):
        
        newFish = countList[0]
        
        for x in range(0, countListSize-1):
            countList[x] = countList[x+1]
            
        countList[6] += newFish
        countList[8] = newFish
        
    #get total fish
    total = 0
    for value in countList:
        total += value
    
    print("Count list: " + str(countList))
    print("Total: " + str(total))

def main():
       
    try:       
        inputFile = open("Day6/input.txt","r")
               
    except:
        print('error opening file')
    
    listOfValues = parseFile(inputFile)
    
    getLanternFishSizeSimulation(listOfValues, 256)
    
       
if __name__ == '__main__':
    main()