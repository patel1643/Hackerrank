def minimumSwaps(arr):
  swapCount = 0
  minPos = 0
  
  for i in range(len(arr)):
    minPos = i
    j = i
    while(j < len(arr)):
      mini = min(arr[j:])
      swapIndex = arr.index(mini)
      if (arr[minPos] != mini):
        temp = arr[minPos]
        arr[minPos] = mini
        arr[swapIndex] = temp
        swapCount+=1
        break
      else:
        break
      
  return swapCount
        
  
print(minimumSwaps([1,3,5,2,4,6,7]))
print(minimumSwaps([2,3,4,1,5]))
print(minimumSwaps([4,3,1,2]))