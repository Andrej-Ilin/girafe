import sys

def n_students(x, d):
    n = 1
    pos = x[0]
    for v in x[1:]:
        if (v - pos) >= d:
            n += 1
            pos = v
    return n
def bin_search(x, M):
    l = 0
    r = max(x)
    while r - l > 1:
        m = (l + r) // 2
        if n_students(x, m) >= M:
            l = m
        else:
            r = m
    return l
if __name__ == '__main__':
    sys.stdin = open('input.txt', 'r')
    N, M = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    print(bin_search(x, M))
