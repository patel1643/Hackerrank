def appleAndOrange(s, t, a, b, apples, oranges):
    appleCounter = 0
    orangeCounter = 0
    for i in apples:
        dist = a + i
        if dist >= s and dist <= t:
            appleCounter += 1
    
    for j in oranges:
        dist = b + j
        if dist >= s and dist <= t:
            orangeCounter += 1
    
    return appleCounter, orangeCounter

#print(appleAndOrange(7, 11,5, 15, [-2,2,1], [5, -6]))