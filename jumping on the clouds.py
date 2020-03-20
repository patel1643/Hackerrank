def jumpingOnTheClouds(c):
    jumpCounter = 0
    i = 0
    
    while(True):
        if i < len(c)-2:
            if c[i+2] == 1:
                i += 1
                jumpCounter +=1
            elif c[i+2] == 0:
                i += 2
                jumpCounter += 1
            if i == len(c)-1:
                break
        else:
            if c[i+1] == 0:
                jumpCounter += 1
                i += 1
            if i == len(c)-1:
                break
    return jumpCounter      


            