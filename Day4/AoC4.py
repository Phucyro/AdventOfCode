


def parseFile(inputFile):
    
    listOfNumbers = inputFile.readline().split(",")
    listOfNumbers[len(listOfNumbers)-1] = listOfNumbers[len(listOfNumbers)-1].rstrip("\n")
    
    
    blank = inputFile.readline()
    
    horizontalLength = 5
    verticalLength = 5
    bingoBoards = []
    
    endInput = False
    
    lineTest = inputFile.readline().split()
    while (not endInput):
        tempBoard = []
        
        tempBoard.append(lineTest)
        
        for i in range(verticalLength-1):
            tempBoard.append(inputFile.readline().split())
        bingoBoards.append(tempBoard)
        
        blank = inputFile.readline().split()
        
        lineTest = inputFile.readline().split()
        
        if len(lineTest) == 0:
            endInput = True
        
       
    
    return listOfNumbers, bingoBoards
    
    
    
def findFirstWinnerBoard(listOfNumbers, bingoBoards):
    
    numberOfBoards = len(bingoBoards)
    boardHorizontalLength = 5
    boardVerticalLength = 5
    
    resultBoards = [[[0 for i in range(boardHorizontalLength)] for j in range(boardVerticalLength)] for k in range(numberOfBoards)]
    
    
    currentNumberPosition = 0
    
    
    boardFinalWinner = None
    lastAnnouncedNumber = None
    found = False
    
    while (not found):
        winningNumber = listOfNumbers[currentNumberPosition]
        
        for boardNumber in range(numberOfBoards):
            
            isWinningNumber = False
            
            #Pour chaque board, voir si on peut trouver une position avec le nombre gagnant
            for xPosition in range(boardHorizontalLength):
                for yPosition in range(boardVerticalLength):
                    if winningNumber == bingoBoards[boardNumber][xPosition][yPosition]:
                        #Si oui, on met à 1 les résultats du board
                        resultBoards[boardNumber][xPosition][yPosition] = 1
                        isWinningNumber = True
                        winningX = xPosition
                        winningY = yPosition
    
                        
            
            if isWinningNumber:
                if isBingo(resultBoards,boardNumber, winningX, winningY):
                    if boardFinalWinner == None:
        
                        boardFinalWinner = boardNumber
                        found = True
                        lastAnnouncedNumber = winningNumber
                    
        currentNumberPosition += 1
        
    
    print("final winner: board number " + str(boardFinalWinner))
    
    totalSumOfUnmarked = 0
    for x in range(5):
        for y in range(5):
            if resultBoards[boardFinalWinner][x][y] == 0:
                totalSumOfUnmarked += int(bingoBoards[boardFinalWinner][x][y])
    
    print("total sum of unmarked: " + str(totalSumOfUnmarked))

def isBingo(resultBoards,boardNumber, winningX, winningY):
    
    result = False
    #verifier la ligne en X
    xSum = 0
    for i in range(5):
        if resultBoards[boardNumber][i][winningY] == 1:
            xSum += 1
    
    #verifier la ligne en Y
    ySum = 0
    for i in range(5):
        if resultBoards[boardNumber][winningX][i] == 1:
            ySum += 1
    
    if xSum == 5 or ySum == 5:
        result = True
    
    return result
        
                    
def findLastWinnerBoard(listOfNumbers, bingoBoards):
    
    numberOfBoards = len(bingoBoards)
    boardHorizontalLength = 5
    boardVerticalLength = 5
    
    resultBoards = [[[0 for i in range(boardHorizontalLength)] for j in range(boardVerticalLength)] for k in range(numberOfBoards)]
                        
    currentNumberPosition = 0
    
    boardFinalLoser = None
    lastAnnouncedNumber = None
    isLastBoard = False
    
    while (not isLastBoard):
        #tant qu'il reste des boards qui n'ont pas fini
        winningNumber = listOfNumbers[currentNumberPosition]
        
        toDeletePosition = []
        
        for boardNumber in range(len(bingoBoards)):
            
            foundCoordinates = False
            
            for xPosition in range(boardHorizontalLength):
                for yPosition in range(boardVerticalLength):
                    if winningNumber == bingoBoards[boardNumber][xPosition][yPosition]:
                        resultBoards[boardNumber][xPosition][yPosition] = 1
                        foundCoordinates = True
                        winningX = xPosition
                        winningY = yPosition
            
            if foundCoordinates:
                if isBingo(resultBoards,boardNumber, winningX, winningY):
                    #si bingo, ajoute la position du board dans la liste "toDeletePosition"
                    toDeletePosition.append(boardNumber)
                
        #Si il restera encore des boards après la suppression, supprimez les boards
        if len(toDeletePosition) < len(bingoBoards):
            for index in reversed(toDeletePosition):
                del bingoBoards[index]
                del resultBoards[index]
        
        #Sinon, on a trouvé le dernier board à gagner
        elif len(toDeletePosition) == len(bingoBoards):
            print("Found last winning board")
            boardFinalLoser = bingoBoards[len(toDeletePosition)-1]
            lastAnnouncedNumber = winningNumber
            isLastBoard = True

        currentNumberPosition += 1
    
            
    
    print("Last winning board: " + str(boardFinalLoser))
    
    totalSumOfUnmarked = 0
    for x in range(5):
        for y in range(5):
            if resultBoards[0][x][y] == 0:
                totalSumOfUnmarked += int(bingoBoards[0][x][y])
                        
    print("Total sum of unmarked: " + str(totalSumOfUnmarked))
    print("Last winning number: " + str(lastAnnouncedNumber))
                    
                    
                        
                    
                
        
    
    
    

def main():
       
    try:       
        inputFile = open("C:/Users/phucy/Desktop/AdventOfCode/Day4/input.txt","r")
        result = parseFile(inputFile)
    except:
        print('error opening file')
        
    
    
    listOfNumbers = result[0]
    bingoBoards = result[1]
    
    findFirstWinnerBoard(listOfNumbers, bingoBoards)
    findLastWinnerBoard(listOfNumbers, bingoBoards)
    
    
    
    
       
if __name__ == '__main__':
    main()