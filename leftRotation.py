
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    firstHalf = []
    lastHalf= []
    final= []
    finalStr = ""
    if(d % n == 0):
        print(a)

    elif (d > 1 and d < n):
        firstHalf = a[d:]
        lastHalf = a[0: d]
    for i in range(len(firstHalf)):
        final.append(firstHalf[i])
    for j in range(len(lastHalf)):
        final.append(lastHalf[j])

    for k in range(len(final)):
        finalStr += str(final[k]) + " "

    print(finalStr)
