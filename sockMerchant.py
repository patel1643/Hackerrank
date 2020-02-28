<<<<<<< HEAD
def sock(arr):
  dic = {}

  for i in arr:
    if i in dic:
      dic[i] = dic[i]+1
    else:
      dic[i] = 1

  counter = 0
  for j in dic:
    if(dic[j] % 2 == 0):
      counter = counter + (dic[j]//2)
    else:
      counter = counter + ((dic[j]-1)//2)
  return counter


print(sock([10, 20, 20, 10, 10, 30, 50, 10, 20]))
=======
def sock(arr):
  dic = {}

  for i in arr:
    if i in dic:
      dic[i] = dic[i]+1
    else:
      dic[i] = 1

  counter = 0
  for j in dic:
    if(dic[j] % 2 == 0):
      counter = counter + (dic[j]//2)
    else:
      counter = counter + ((dic[j]-1)//2)
  return counter


print(sock([10, 20, 20, 10, 10, 30, 50, 10, 20]))
>>>>>>> ee91439573c15df174e8dff8871aedcc60dad00b
