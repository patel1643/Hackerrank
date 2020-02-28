def plusMinus(arr):
    positiveCount = 0
    negativeCount = 0
    zeroCount = 0
    size = len(arr)
    for i in arr:
        if i < 0:
            negativeCount += 1
        elif i > 0:
            positiveCount += 1
        else:
            zeroCount += 1
    
    posRatio = round(positiveCount / size, 6)
    negRatio = round(negativeCount / size, 6)
    zeroRatio = round(zeroCount / size, 6)

    print(posRatio)
    print(negRatio)
    print(zeroRatio)
