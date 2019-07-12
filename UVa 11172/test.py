#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def RelationalOperator(a, b): 
    if a != b :
        if a>b :
            return ">"
        else :
            return "<"
    else :
        return "="
    
if __name__ == '__main__':

    fptr = open('myoutput', 'w')

    n = list(map(int, input().rstrip().split()))
	    # print(n)
    for i in range(0,n[0]): 

        a = list(map(int, input().rstrip().split()))
        
        result = RelationalOperator(a[0], a[1])

        fptr.write(' '.join(map(str, result)))

        fptr.write('\n')

    fptr.close()

