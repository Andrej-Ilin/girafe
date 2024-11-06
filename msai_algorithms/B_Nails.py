def nails(x, N):
    x = sorted(x)
    d = [inf]*N

    d[1] = x[1] - x[0]
    for i in range(2, N):
        d[i] = min(d[i - 2], d[i - 1]) + x[i] - x[i - 1]
    return d[-1]

if __name__ == '__main__':
    import sys
    from math import inf
    sys.stdin = open('input.txt', 'r')
    N = int(input().strip())
    x = list(map(int, input().strip().split()))
    print(nails(x, N))