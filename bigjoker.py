def move_big_joker(arr):
  #i am using arr parameter as a list or an array
  # just for clarification lol
  maxi = 0 #maximum

  for i in arr:
    if i > maxi:
      maxi = i

  for k in range(len(arr)):
    if arr[k] == maxi:
      if(k < len(arr) - 2):
        temp = arr[k+1]
        temp2 = arr[k+2]
        arr[k] = temp
        arr[k+1] = temp2
        arr[k+2] = maxi
        break
      elif(k == len(arr) - 2):
        temp3 = arr[k+1]
        temp4 = arr[k+2]
        arr[0] = maxi
        arr[k] = temp3
        arr[k+1] = temp4
        break
      else:
        temp5 = arr[1]
        temp6 = arr[0]
        arr[0] = temp5
        arr[k] = temp6
        arr[1] = maxi
        break

  return arr

print(move_big_joker([2,8,5,3,6,1,4,7]))
