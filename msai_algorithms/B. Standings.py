import random


def partition(x, l, r, pivot):
    """
    :param x: Source array (list)
    :param l: left border of partitioning range (int)
    :param r: right border (not included) of partitioning range (int)
    :param pivot: pivot element to divide array (any item from x[l, r)).
    :return: il, ir -- desired partition
    This function should reorder elements of x within [l, r) region
    in the way, these conditions are true:
    x[l:il] < pivot
    x[il:ir] == pivot
    x[ir:r] > pivot
    """
    # Your code goes here
    il = l  # index for less than pivot
    ir = l  # index for equal to pivot

    for i in range(l, r):
        if x[i] < pivot:
            x[il], x[i] = x[i], x[il]  # swap to the left
            if il < ir:
                x[ir], x[i] = x[i], x[ir]  # swap equal to pivot after il
            il += 1
            ir += 1
        elif x[i] == pivot:
            x[ir], x[i] = x[i], x[ir]  # swap equal to pivot
            ir += 1
    
    return il, ir



def qsort(x, l=0, r=None):
    if r is None:
        r = len(x)
    if (r - l) > 1:
        pivot = x[random.randint(l, r - 1)]
        il, ir = partition(x, l, r, pivot)
        qsort(x, l, il)
        qsort(x, ir, r)


if __name__ == '__main__':
    N = int(input())
    x = list(map(int, input().split()))
    qsort(x)
    print(' '.join(map(str, x)))