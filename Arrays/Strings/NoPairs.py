#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minimalOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY words as parameter.
#

def minimalOperations(words):
    
    retArr = []
    
    for word in words:
        
        minChanges = 0
        
        n = len(word)
        
        i = 0
        
        while i < n-1:
            
            # Same Letter
            if word[i] == word[i+1]:
                
                # Three in a row
                if i+2 < n:
                    if word[i+2] == word[i]:
                        minChanges+=1
                        i+=2
                    else:
                        minChanges+=1
                        i+=2
                        
                else:
                    minChanges+=1
                    i+=1
            
            else:
                i+=1
                        
        retArr.append(minChanges)
        
    return retArr
        

if __name__ == '__main__':
    
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    words_count = int(input().strip())

    words = []

    for _ in range(words_count):
        words_item = input()
        words.append(words_item)

    result = minimalOperations(words)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
