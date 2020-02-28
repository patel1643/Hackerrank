def diagonalDifference(arr):
    # Write your code here
    leftSum = 0
    rightSum = 0

    notDone = True
    i = 0
    j = 0
    k = 0
    l = len(arr) -1 

    while(notDone):
        leftSum = leftSum + arr[i][j]
        rightSum = rightSum + arr[k][l]
        i += 1
        j += 1
        k += 1
        l -= 1
        if l < 0:
            notDone = False

    difference = leftSum - rightSum
    if(difference < 0):
        difference = difference * (-1)

    return difference
