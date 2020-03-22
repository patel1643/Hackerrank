def makeAnagram(a,b):
    counter = 0
    for i in a:
        if i not in b:
            counter += 1
            a = a.replace(i,"")
    for j in b:
        if j not in a:
            counter += 1
            b = b.replace(j,"")
    print(a, b)
    return counter

print(makeAnagram("jxwtrhvujlmrpdoqbisbwhmgpmeoke","fcrxzwscanmligyxyvym"))