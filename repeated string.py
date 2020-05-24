def repeatedString(s, n):
    if len(s) == 1 and s == "a":
        return n
    else:
        counter = 0
        newS = s * (n//len(s)+1)
        newS = newS[:n]
        
        for i in newS:
            if i == "a":
                counter += 1
        return counter
    
print(repeatedString("anna",100))