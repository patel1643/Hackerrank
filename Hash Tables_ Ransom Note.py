def checkMagazine(magazine, note):
    magDict = {}
    checkCounter = 0
    for i in magazine:
        magDict[i] = None
            
    for j in note:
        if j in magDict:
            checkCounter+=1
            magDict.pop(j)
    
    if checkCounter >= len(note):
        return "Yes"
    else:
        return "No"
            
