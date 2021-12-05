def getMaxHorinzontalAndVerticalValues(ventsLines):
    
    maxX = 0
    maxY = 0
    
    for x in range(len(ventsLines)):
        
        tempLine = ventsLines[x]
        
        maxLineX = max(int(tempLine[0][0]), int(tempLine[1][0]))
        maxLineY = max(int(tempLine[0][1]), int(tempLine[1][1]))
        
        if maxX < maxLineX:
            maxX = maxLineX
        if maxY < maxLineY:
            maxY = maxLineY
    
    return maxX, maxY

def getCountBoard(maxX, maxY):
    
    result = [[0 for i in range(maxY+1)] for j in range(maxX+1)]
    
    return result



def getOverlappedPoints(ventsLines):
    
    maxX, maxY = getMaxHorinzontalAndVerticalValues(ventsLines)
    
    resultCountBoard = getCountBoard(maxX, maxY)
    
    for x in range(len(ventsLines)):
        
        firstXValue = int(ventsLines[x][0][0])
        secondXValue = int(ventsLines[x][1][0])
        
        firstYValue = int(ventsLines[x][0][1])
        secondYValue = int(ventsLines[x][1][1])
        
        #ligne horizontale trouvée
        if firstXValue == secondXValue:
            
            #inverser les valeurs pour le for in range suivant
            #si nécessaire (lorsque le premier point se trouve à droite)
            if firstYValue > secondYValue:
                tempYValue = firstYValue
                firstYValue = secondYValue
                secondYValue = tempYValue
                
            #ajout de 1 sur toute la ligne horizontale dans le resultCountBoard
            for i in range(firstYValue, secondYValue+1):
                resultCountBoard[firstXValue][i] += 1

        #ligne verticale trouvée
        if firstYValue == secondYValue:
            
            #inverser les valeurs pour le for in range suivant
            #si nécessaire (lorsque le premier point se trouve à droite)
            if firstXValue > secondXValue:
                tempXValue = firstXValue
                firstXValue = secondXValue
                secondXValue = tempXValue
                
            #ajout de 1 sur toute la ligne verticale dans le resultCountBoard
            for i in range(firstXValue,secondXValue+1):
                resultCountBoard[i][firstYValue] += 1
                
        #Regarder si la ligne est diagonale
        if abs(firstXValue-secondXValue) == abs(firstYValue-secondYValue):
            
            #Inverser les coordonnées si nécessaires
            #pour avoir en premier celui qui a le X le plus faible
            if firstXValue > secondXValue:
                #inverser X
                tempValueX = firstXValue
                firstXValue = secondXValue
                secondXValue = tempValueX
                #inverser Y
                tempValueY = firstYValue
                firstYValue = secondYValue
                secondYValue = tempValueY
            
            #vérifier si diagonale montante ou descendante
            
            if firstYValue < secondYValue:
                #diagonale montante  
                currentIncrement = 0
                for i in range(firstXValue, secondXValue+1):
                    resultCountBoard[i][firstYValue+currentIncrement] += 1
                    currentIncrement+=1
            
            if firstYValue > secondYValue:
                #diagonale descendante
                currentIncrement = 0
                for i in range(firstXValue, secondXValue+1):
                    resultCountBoard[i][firstYValue-currentIncrement] += 1
                    currentIncrement+=1
                
            
    totalOverlap = 0
    for x in range(len(resultCountBoard)):
        for y in range(len(resultCountBoard[0])):
            if resultCountBoard[x][y] > 1:
                totalOverlap += 1
    print("totalOverlap: " + str(totalOverlap))

def parseFile(inputFile):
    
    ventsLines = []
    
    for line in inputFile:
        
        tempLineList = []
        tempLine = line.split()
        
        del tempLine[1] #remove the arrow
        start = tempLine[0].split(",")
        end = tempLine[1].split(",")
        
        tempLineList.append(start)
        tempLineList.append(end)
    
        ventsLines.append(tempLineList)

    return ventsLines

def main():
       
    try:       
        inputFile = open("C:/Users/phucy/Desktop/AdventOfCode/Day5/input.txt","r")
        result = parseFile(inputFile)
        getOverlappedPoints(result)
        
    except:
        print('error opening file')
    
    
       
if __name__ == '__main__':
    main()