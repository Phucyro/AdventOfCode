def parseFile(inputFile):
    
    result = inputFile.readline().split(",")
    
    for i in range(len(result)):
        result[i] = int(result[i])
    
    return result


    

def findOptimalPosition(positions):
    
    dictPositionValues = dict()
    
    minDistance = None
    minPosition = None
    
    for i in range(max(positions)+1):
        totalDistance = 0
        for j in range(len(positions)):    
            HigherPosition = max(i,positions[j])
            LowerPosition = min(i,positions[j]) 
                
            distance = HigherPosition - LowerPosition 
                
            temp = 0
                
            for k in range(1, distance+1, 1):
                totalDistance += k                    
                temp += k
                    
            if i == 0 and j == 1:
                print("here")
                print(i)
                print(positions[j])                    
                print(HigherPosition)
                print(LowerPosition)
                print(distance)
                print(temp)        
                
                    
            
        if minDistance == None or totalDistance < minDistance:
            minDistance = totalDistance
            minPosition = positions[i]
                
            
                    
            
        
    
    print(minPosition, minDistance)
         
        

def main():
       
    try:       
        inputFile = open("Day7/input.txt","r")
               
    except:
        print('error opening file')
    
    listOfValues = parseFile(inputFile)
    findOptimalPosition(listOfValues)
    
       
if __name__ == '__main__':
    main()