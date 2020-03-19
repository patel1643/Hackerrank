def minimumSwaps2(arr):
    swapCount = 0
    minPos = 0
    
    for i in range(len(arr)):
        mini = min(arr[i:])
        swapIndex = arr.index(mini)
        
        if arr[i] != mini:
            temp = arr[i]
            arr[i] = mini
            arr[swapIndex] = temp
            swapCount += 1
            
    return swapCount

print(minimumSwaps2([1,3,5,2,4,6,7]))
print(minimumSwaps2([2,3,4,1,5]))
print(minimumSwaps2([4, 5, 2, 1, 5]))