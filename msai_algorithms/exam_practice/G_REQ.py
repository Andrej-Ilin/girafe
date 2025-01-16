"""It solve was only experiment  with AI Claude3.5 Sonnet, but not mine!!!"""
class Node:
    def __init__(self):
        self.counts = {}  # Dictionary to store count of each value


class SegmentTree:
    def __init__(self, arr, K):
        self.n = len(arr)
        self.K = K
        self.tree = [Node() for _ in range(4 * self.n)]
        self.build(arr, 0, 0, self.n)

    def merge(self, left, right):
        result = Node()
        # Merge counts from left and right children
        for k in range(self.K + 1):
            result.counts[k] = left.counts.get(k, 0) + right.counts.get(k, 0)
        return result

    def build(self, arr, v, tl, tr):
        if tl + 1 == tr:
            self.tree[v].counts[arr[tl]] = 1
            return

        tm = (tl + tr) // 2
        self.build(arr, 2 * v + 1, tl, tm)
        self.build(arr, 2 * v + 2, tm, tr)
        self.tree[v] = self.merge(self.tree[2 * v + 1], self.tree[2 * v + 2])

    def update(self, pos, old_val, new_val, v, tl, tr):
        if tl + 1 == tr:
            self.tree[v].counts[old_val] = 0
            self.tree[v].counts[new_val] = 1
            return

        tm = (tl + tr) // 2
        if pos < tm:
            self.update(pos, old_val, new_val, 2 * v + 1, tl, tm)
        else:
            self.update(pos, old_val, new_val, 2 * v + 2, tm, tr)
        self.tree[v] = self.merge(self.tree[2 * v + 1], self.tree[2 * v + 2])

    def query(self, l, r, k, v, tl, tr):
        if l >= tr or r <= tl:
            return 0
        if l <= tl and tr <= r:
            return self.tree[v].counts.get(k, 0)

        tm = (tl + tr) // 2
        return (self.query(l, r, k, 2 * v + 1, tl, tm) +
                self.query(l, r, k, 2 * v + 2, tm, tr))


def solve():
    # Read input
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))

    # Initialize segment tree
    seg_tree = SegmentTree(arr, K)

    # Process queries
    for _ in range(M):
        query = input().split()
        if query[0] == '?':
            l, r, k = map(int, query[1:])
            print(seg_tree.query(l, r, k, 0, 0, N))
        else:  # '+'
            i, delta = map(int, query[1:])
            old_val = arr[i]
            new_val = old_val + delta
            arr[i] = new_val
            seg_tree.update(i, old_val, new_val, 0, 0, N)


if __name__ == "__main__":

    solve()