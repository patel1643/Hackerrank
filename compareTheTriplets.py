def compareTriplets(a, b):
    alice = 0
    bob = 0
    resultArr = []
    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    resultArr.append(alice)
    resultArr.append(bob)
    return resultArr
