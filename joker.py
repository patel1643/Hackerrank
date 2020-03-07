def move_small_joker(arr):
  #i am using arr parameter as a list or an array
  # just for clarification lol
  maxi = 0 #maximum
  mid = 0 #secondHighest number

  for i in arr:
    if i > maxi:
      maxi = i

  for j in range(len(arr)):
    if arr[j] < maxi and arr[j] > mid:
      mid = arr[j]

  for k in range(len(arr)):
    if arr[k] == mid:
      if(k < len(arr) - 1):
        temp = arr[k+1]
        arr[k] = temp
        arr[k+1] = mid
        break
      else:
        temp1 = arr[0]
        arr[0] = mid
        arr[k] = temp1
        break

  return arr
