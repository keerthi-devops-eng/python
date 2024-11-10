#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    weights = dict(zip(alphabet, range(1, 27)))
    result = []
    prev_char = ''
    current_weight = 0
    uniform_weights = set()
    
    for char in s:
        if char == prev_char:
            current_weight += weights[char]
        else:
            current_weight = weights[char]
            prev_char = char
        uniform_weights.add(current_weight)
        
    for q in queries:
        if q in uniform_weights:
            result.append("Yes")
        else:
            result.append("No")
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
