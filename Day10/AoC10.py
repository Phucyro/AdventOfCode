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
        "<":">"
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
        
                    

def main():
       
    try:       
        inputFile = open("Day10/input.txt","r")
               
    except:
        print('error opening file')
    
    listOfValues = parseFile(inputFile)
    
    findIllegalSyntax(listOfValues)
    
       
if __name__ == '__main__':
    main()