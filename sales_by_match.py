

import math
import os
import random
import re
import sys



def sockMerchant(n, ar):
    count = {}

    for color in ar:
        if color in count:
            count[color] += 1
        else:
            count[color] = 1

    pairs = 0

    for color in count:
        pairs += count[color] // 2

    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
