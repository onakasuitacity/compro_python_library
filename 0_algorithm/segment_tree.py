# segment tree (without lazy-propagation)
# cf. https://github.com/onakasuitacity/atcoder_py/blob/master/0_algorithm/lazy_propagation_segment_tree.py
class SegmentTree(object):
    def __init__(self, arr, dot, e):
        n = 1
        while n < len(arr):
            n <<= 1
        tree = [e] * (2 * n)
        for i, v in enumerate(arr):
            tree[i + n] = v
        for i in range(n - 1, 0, -1):
            tree[i] = dot(tree[2 * i], tree[2 * i + 1])
        self.n = n
        self.tree = tree
        self.dot = dot
        self.e = e
    
    def __getitem__(self, i):
        return self.tree[i + self.n]
    
    def update(self, i, v):
        i += self.n
        self.tree[i] = v
        while i != 1:
            p = i // 2
            self.tree[p] = self.dot(self.tree[2 * p], self.tree[2 * p + 1])
            i = p
    
    def sum(self, l, r):
        l += self.n
        r += self.n
        l_val = r_val = self.e
        while l < r:
            if l & 1:
                l_val = self.dot(l_val, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                r_val = self.dot(self.tree[r], r_val)
            l >>= 1
            r >>= 1
        return self.dot(l_val, r_val)

# example
A=[4,9,11,5,13,33,33,33,11,45,14,19,19,8,10,89]
dot=min
e=float("inf")
tree=SegmentTree(A,dot,e)
print(tree.bisect(3,13,12,increase=False))
