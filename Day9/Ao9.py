def parseFile(inputFile):
    
    res = []
    for line in inputFile:
        
        res.append(line.strip())
            
    return res

def isValidPosition(position,maxX, maxY):
    
    xPosition = position[0]
    yPosition = position[1]
    
    return (xPosition >=0 and xPosition < maxX and yPosition < maxY and yPosition >= 0)

def findRisk(listOfValues):
    
    maxY = len(listOfValues)
    maxX = len(listOfValues[0])
    
    totRisk = 0
    lowPointList = []
    
    for y in range(len(listOfValues)):
        for x in range(len(listOfValues[y])):
            
            positions = (x, y+1), (x,y-1), (x-1, y),(x+1,y)
            isLowPoint = True
            
            for position in positions:
                if isValidPosition(position, maxX, maxY):
                    
                    if int(listOfValues[position[1]][position[0]]) <= int(listOfValues[y][x]):
                        isLowPoint = False
            
            if (isLowPoint):
                totRisk += int(listOfValues[y][x]) + 1
                lowPointList.append((y,x))
                
    print(lowPointList)
    print(totRisk)
            
    #PART 2
    findBassins(lowPointList, listOfValues, maxX, maxY)
    
def findBassins(lowPointList, listOfValues, maxX, maxY):
    
    lowPointBassin = {}
    
    for points in lowPointList:
        yPos = points[0]
        xPos = points[1]
        lowPointBassin[(yPos,xPos)] = []
        
        isBlocked = False
        toDo = [(yPos,xPos)]
        DoneList = []
        while (not isBlocked):
            print(toDo)
            isBlocked = True
            toRemove = []
            for position in toDo:
                
                toDoY = position[0]
                toDoX = position[1]
                
                incrementPosition = (position[0], position[1]+1), (position[0]+1, position[1]+1), (position[0]+1, position[1]), (position[0]+1, position[1]-1), (position[0], position[1]-1), (position[0]-1,position[1]-1), (position[0]-1, position[1]), (position[0]-1, position[1]+1)
                
                for positionToVerify in incrementPosition:
                    yTemp = positionToVerify[0]
                    xTemp = positionToVerify[1]
                    
                    if isValidPosition((xTemp,yTemp), maxX, maxY) and (yTemp, xTemp) not in lowPointBassin[(yPos,xPos)] and (yTemp,xTemp) not in DoneList and int(listOfValues[yTemp][xTemp]) != 9:
                        #found new part of passin
                        toDo.append((yTemp,xTemp))
                        lowPointBassin[(yPos,xPos)].append((yTemp,xTemp))
                        isBlocked = False
                    
                    else:
                        DoneList.append((yTemp,xTemp))
                
                toRemove.append(position)
            
            for elem in toRemove:
                toDo.remove(elem)
        
    for keys in lowPointBassin.keys():
        print(len(lowPointBassin[keys]))
                        
                        
                                                               
                    
                    
                        
                    

            
            
            
           
    
    print(lowPointBassin)
            
            
            
        
    print(lowPointBassin)
        
        
                      
            
def main():
       
    try:       
        inputFile = open("Day9/input.txt","r")
               
    except:
        print('error opening file')
    
    listOfValues = parseFile(inputFile)
    findRisk(listOfValues)
    
    
    
    
       
if __name__ == '__main__':
    main()