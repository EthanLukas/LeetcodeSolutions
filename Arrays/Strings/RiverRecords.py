#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxTrailing' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxTrailing(arr):
    
    n = len(arr)
    
    if n == 0 or n==1:
        return -1
    
    result = -1
    
    l = 0
    r = 1
    
    minLeft = arr[0]
    
    while r < n:
        
        if arr[r] > minLeft:
            
            diff = arr[r]-minLeft
            
            if diff > result:
                result = diff
        
        elif arr[r] == minLeft:
            pass
                
        else:
            minLeft = arr[r]
            
        r+=1
        
                
        
    
        # Valid
        # if arr[l] < arr[r]:
        #     if arr[r] - arr[l] > result:
        #         result = arr[r] - arr[l]
            
        # else:
        #     r+=1
    
    # for i in range(n):
    #     if i+1 < n:
    #         for j in range(i+1, n):
    #             if arr[j] > arr[i]:
    #                 diff = arr[j] - arr[i]
    #                 if diff > result:
    #                     result = diff
    
    return result
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxTrailing(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
