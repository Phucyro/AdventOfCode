def parseFile(inputFile):
    result = []
    
    for line in inputFile:
        result.append(line.strip().split("|"))
    
    return result
    
def findUniqueSegments(signals):
    
    totalUnique = 0
    
    for x in range(len(signals)):
        uniqueValues = dict()
        result = dict()
        lenghtOf5 = []
        lengthOf6 = []
        
        #FIND START
        toDecode = signals[x][0].split()
        outputValues = signals[x][1].split()
        
        
        for value in toDecode:
            if len(value) == 2:
                uniqueValues[1] = value
            
            elif len(value) == 3:
                uniqueValues[7] = value
            
            elif len(value) == 4:
                uniqueValues[4] = value
            
            elif len(value) == 7:
                uniqueValues[8] = value
            
     
            
        #DECODE
        #Si 1 et 7 existe, la barre du haut (a) est d'office la lettre en plus
        if 1 in uniqueValues.keys() and 7 in uniqueValues.keys():
            
            tempSignal = uniqueValues[7]
            wrongLetter = None
            for lettre in tempSignal:
                if not(lettre in uniqueValues[1]):
                    wrongLetter = lettre
                    result["a"] = wrongLetter
                
        for value in toDecode:
            if len(value) == 5:
                lenghtOf5.append(value)
            elif len(value) == 6:
                lengthOf6.append(value)
        
        #trouver le 3 grâce au 1
        for value in lenghtOf5:
            if uniqueValues[1][0] in value and uniqueValues[1][1] in value:
                uniqueValues[3] = value
        
        #et donc trouver la valeur de la barre du milieu (d)
        #et ainsi déduire l'autre barre ()
        
        tempValue1 = set(uniqueValues[1])
        tempValue2 = set(uniqueValues[4])
        difference = tempValue1.symmetric_difference(tempValue2)
                
        foundLetterD = None
        foundLetterB = None
        
        for lettre in difference:
            if lettre in uniqueValues[3]:
                foundLetterD = lettre
        
        difference.remove(foundLetterD)
        foundLetterB = difference.pop()
                
        result["d"] = foundLetterD
        result["b"] = foundLetterB
        
        #trouver le 5 grâce à barre a, d et b
        #trouver où se trouve la barre du 1
        for value in lenghtOf5:
            if result["a"] in value and result["d"] in value and result["b"] in value:
                uniqueValues[5] = value
        
        tempString = result["a"]+result["d"]+result["b"]
        tempString = set(tempString)
        tempVal2 = set(uniqueValues[5])
        
        diff = tempString.symmetric_difference(tempVal2)
        
        #trouver barre F et G
        foundF = None
        foundG = None
        
        for lettre in diff:
            if lettre in uniqueValues[1]:
                foundF = lettre
        
        diff.remove(foundF)
        foundG = diff.pop()
                        
        result["f"] = foundF
        result["g"] = foundG
        
        
        #find other part of 1 (c)
        tempVeryVal = set(result["f"])
        tempVeryVal2 = set(uniqueValues[1])
        veryDiff = tempVeryVal.symmetric_difference(tempVeryVal2)
        
        foundC = veryDiff.pop()
        result["c"] = foundC
        
        #find (2) -> diff 9 et 8
        
        tempStringSearch = result["a"]+result["b"]+result["c"]+result["d"]+result["f"]+result["g"]
        tempStringSearch = set(tempStringSearch)
        
        tempoValue = set(uniqueValues[8])
        
        foundE = tempStringSearch.symmetric_difference(tempoValue)
        foundE = foundE.pop()
        
        result["e"] = foundE
        
        res = getOutput(outputValues,result)
        
        
        totalUnique+= int(res)
        
        
    print(totalUnique)
    
def sortString(string):
    stringSorted = ''.join(sorted(string))
    return stringSorted
    
def getOutput(outputValues, result):
    
    repOf5 = result["a"]+result["b"]+result["d"]+result["f"]+result["g"]
    repOf2 = result["a"]+result["c"]+result["d"]+result["e"]+result["g"]
    repOf3 = result["a"]+result["c"]+result["d"]+result["f"]+result["g"]
    repOf6 = result["a"]+result["b"]+result["d"]+result["e"]+result["g"]+result["f"]
    repOf9 = result["a"]+result["b"]+result["c"]+result["d"]+result["f"]+result["g"]
    repOf0 = result["a"]+result["b"]+result["c"]+result["e"]+result["f"]+result["g"]
    
    repDic = {
        5: sortString(repOf5),
        2: sortString(repOf2),
        3: sortString(repOf3),
        6: sortString(repOf6),
        9: sortString(repOf9),
        0: sortString(repOf0)
    }
    
    res = ""
    
    for value in outputValues:
        if len(value) == 2:
            res += str(1)
        elif len(value) == 3:
            res += str(7)
        elif len(value) == 4:
            res += str(4)
        elif len(value) == 7:
            res += str(8)
        
        else:
            value = sortString(value)
            
            for key in repDic:
                if value == repDic[key]:
                    res+= str(key)
    
    return res
    

def main():
       
    try:       
        inputFile = open("Day8/input.txt","r")
               
    except:
        print('error opening file')
    
    listOfValues = parseFile(inputFile)
    
    findUniqueSegments(listOfValues)
    
    
       
if __name__ == '__main__':
    main()