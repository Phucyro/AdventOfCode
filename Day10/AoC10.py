def parseFile(inputFile):
    
    res = []
    
    for line in inputFile:
        res.append(line.strip())
        
    return res

def findIllegalSyntax(listOfValues):
    
    leftSymbols = ["(", "[", "{", "<"]
    rightSymbols = [")", "]", "}", ">"]
    
    correspondingSymbols = {
        "(":")",
        "[":"]",
        "{":"}",
        "<":">",
        ")":"(",
        "]":"[",
        "}":"{",
        ">":"<" 
    }
    
    errorFoundList = []
    print(listOfValues)
    
    for line in listOfValues:
        
        symboleList = []
        foundError = False
        increment = 0
        while (not foundError) and increment < len(line):
            
            value = line[increment]
            if value in leftSymbols:
                symboleList.append(value)
            elif value in rightSymbols:
                tempLeft = symboleList.pop()
                
                if (correspondingSymbols[tempLeft] != value):
                    errorFoundList.append(value)
                    foundError = True
                    
            increment += 1
            
            if increment == len(line):
                print("no error found")
                errorFoundList.append(None)
           
    
    totalError = 0
    for error in errorFoundList:
        if error == None:
            continue
        elif error == ")":
            totalError += 3
        elif error == "]":
            totalError += 57
        elif error == "}":
            totalError += 1197
        elif error == ">":
            totalError += 25137
        
    
    print(errorFoundList)
    print("Total error: ", totalError)
    
    completeMissing(listOfValues, errorFoundList)
        
def completeMissing(listOfValues, errorFoundList):
    
    leftSymbols = ["(", "[", "{", "<"]
    rightSymbols = [")", "]", "}", ">"]
    
    correspondingSymbols = {
        "(":")",
        "[":"]",
        "{":"}",
        "<":">",
        ")":"(",
        "]":"[",
        "}":"{",
        ">":"<" 
    }
    
    errorCount = {
        ")":1,
        "]":2,
        "}":3,
        ">":4
    }
    
    dicoResult = {}
    testCount = 0
    result = []
    
    for i in range(len(listOfValues)):
        if errorFoundList[i] == None:
            print(i)
            #COMPLETe THOSES.
            symboleList = []
            isFinished = False
            increment = 0

            sequence = listOfValues[i]
            while (not isFinished) and increment < len(sequence):
                
                value = sequence[increment]
                
                if value in leftSymbols:
                    symboleList.append(value)
                elif value in rightSymbols:
                    tempLeft = symboleList.pop()
                    
                increment += 1
            
            added = ""
            
            for i in range(len(symboleList)):
                added += correspondingSymbols[symboleList.pop()]
            
            
            
            result.append(added)
    
    print(result)
    
    #calculate error result
    scoreResult = []

    for sequence in result:
        
        totalScore = 0
        for symbole in sequence:
            totalScore *= 5
            totalScore += errorCount[symbole]
            
        scoreResult.append(totalScore)
    
    scoreResult.sort()
    
    index = int((len(scoreResult)-1)/2)
    print(scoreResult[index])
    
    
    
def main():
       
    try:       
        inputFile = open("Day10/input.txt","r")
               
    except:
        print('error opening file')
    
    listOfValues = parseFile(inputFile)
    
    findIllegalSyntax(listOfValues)
    
       
if __name__ == '__main__':
    main()