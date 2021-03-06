#!/bin/python3

import math
import os
import random
import re
import sys
 
# URL: https://www.hackerrank.com/challenges/dynamic-array/problem
#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    arr = [];
    answers = [];
    lastAnswer = 0;
    for i in range(n):
        arr.append([]);
    
    for query in queries:
        if (query[0] == 1):
            idx = ((query[1]^lastAnswer)%n);
            arr[idx].append(query[2]);
        if (query[0] == 2):
            idx = ((query[1]^lastAnswer)%n);
            lastAnswer = arr[idx][query[2]%len(arr[idx])];
            answers.append(lastAnswer);
    return answers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
