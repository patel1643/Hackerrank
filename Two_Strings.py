def twoStrings(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    
    for i in s1:
        if i in s2:
            return "YES"
    return "NO"
            
print(twoStrings("hello","world"))