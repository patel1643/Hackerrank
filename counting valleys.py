def countingValleys(n,S):
    heightCounter = 0
    valleyCounter = 0
    previousCount = 0
    
    for i in range(n):
        previousCount = heightCounter
        if S[i] == "U":
            heightCounter += 1
        elif S[i] == "D":
            heightCounter -= 1
        if i > 0:
            if (heightCounter == 0 and previousCount < 0):
                valleyCounter += 1
    return valleyCounter


