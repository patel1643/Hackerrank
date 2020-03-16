def miniMaxSum(arr):
    minTotal = 0
    maxTotal = 0
   # total = 0
    arr = sorted(arr)

    for i in range(len(arr)):
        if i < len(arr)-1:
            minTotal += arr[i]
        if i > 0:
            maxTotal += arr[i]
    
    print(minTotal, maxTotal)
