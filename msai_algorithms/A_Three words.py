import sys
from math import isinf

from bisect import bisect_left
import math


def lis(x, N):
    # N = len(x)
    # Initialize a list 'd' with positive infinity, with a length of N + 1
    d = [math.inf] * (N + 1)
    # print(d)
    # Set the first element to negative infinity to act as a sentinel
    d[0] = -math.inf
    # print(d)
    for i in range(N):
        # Use binary search to find the smallest index l* such that d[l*] >= x[i]
        l_star = bisect_left(d, x[i])
        # Update d[l_star] with x[i]
        # print(d)
        d[l_star] = x[i]

    # Find the largest index l where d[l] is less than infinity
    lis_length = max(l for l in range(N + 1) if d[l] < math.inf)
    return lis_length



if __name__ == '__main__':
    sys.stdin = open('input.txt', 'r')
    N = int(input().strip())
    x = list(map(int, input().strip().split()))
    print(lis(x, N))