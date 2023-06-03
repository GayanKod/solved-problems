#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr): 
    # Write your code here
    countPositive = 0
    countNegative = 0
    countZeros = 0
    n = len(arr)
    
    #Check and count
    for i in arr:
        if (i<0):
            countNegative+=1
        elif (i==0):
            countZeros+=1
        else:
            countPositive+=1
    
    #Output
    print("{:.6f}".format(round(countPositive/n, 6)))
    print("{:.6f}".format(round(countNegative/n, 6)))
    print("{:.6f}".format(round(countZeros/n, 6)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
