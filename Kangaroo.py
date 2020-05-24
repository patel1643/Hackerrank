def kangaroo(x1, v1, x2, v2):
    if (x1 < x2):
        if(v2 > v1):
            return "NO"
        else:
            return "YES"
    elif (x1 > x2):
        if(v2 < v1):
            return "NO"
        else:
            return "YES"
        
    

        