#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def displayHourglass(arr, row, col):
    top = row;
    mid = row + 1;
    bottom = row + 2;
    
    topHourglass = arr[top][col:3 + col]
    midHourglass = arr[mid][(col+1):2 + col]
    bottomHourglass = arr[bottom][col:3+ col]
    
    return [topHourglass, midHourglass, bottomHourglass]

def addHourGlassValues(arrs):
    hourglassSum = 0;
    for i in range(len(arrs)):
        for j in range(len(arrs[i])):
            hourglassSum += arrs[i][j];
    return hourglassSum
    
def hourglassSum(arr):
    max_col = 4
    max_row = 4
    
    highestValue = float('-inf');
    for i in range(max_row):
        for j in range(max_col):
            hourGlass = displayHourglass(arr, i, j);
            tempValue = addHourGlassValues(hourGlass)
            if(tempValue > highestValue):
                highestValue = tempValue;
                
    return highestValue
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
