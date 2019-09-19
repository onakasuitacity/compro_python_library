# bin sort O(max(A)-min(A)+len(A))
# https://engineeringnote.hateblo.jp/entry/python/algorithm-and-data-structures/bin_sort
def bin_sort(A,n_min=None,n_max=None):
    """
    A: list of integer
    n_min: minimum of A
    n_max: maximum of A
    """
    if n_min is None: n_min=min(A)
    if n_max is None: n_max=max(A)
    bin=[0]*(n_max-n_min+1)
    for a in A: bin[a]+=1
    B=[]
    for i in range(n_min,n_max+1): B+=[i]*bin[i]
    return B

# input
A=[3,-5,8,2,3,8,-4,-3,0,-3,5]
print(bin_sort(A)) # [-5,-4,-3,-3,0,2,3,3,5,8,8]
