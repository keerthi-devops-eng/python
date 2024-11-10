#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def numCells(grid):
    
    rows = len(grid)
    columns = len(grid[0])
    dominant = 0
    
    if not grid:
        return 0
    
    if rows == 1 and columns == 1:
        return 1
    
    for i in range(rows):
        for j in range(columns):
            # if (i == rows - 1 or grid[i][j] > grid[i+1][j]) and \
            #    (j == columns -1 or grid[i][j] > grid[i][j+1]) and \
            #    (i == 0 or grid[i][j] > grid[i-1][j]) and \
            #    (j == 0 or grid[i][j] > grid[i][j-1]):
            isdominant = True
            for x in range(max(0, i-1), min(rows, i+2)):
                for y in range(max(0, j-1), min(columns, j+2)):
                    if grid[x][y] >= grid[i][j] and (x, y)!=(i, j):
                        isdominant = False
            if isdominant:
                dominant+=1
    return dominant

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
