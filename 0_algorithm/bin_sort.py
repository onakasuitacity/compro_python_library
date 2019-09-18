# bin sort (O(max(A)))
# https://engineeringnote.hateblo.jp/entry/python/algorithm-and-data-structures/bin_sort
def bin_sort(A,n_max=max(A)):
    """
    A: list of non-negative int
    n_max: maximum of A
    """
    bin=[0]*(n_max+1)
    for a in A: bin[a]+=1
    B=[]
    for i in range(n_max+1): B+=[i]*bin[i]
    return B

# input
A=[3,5,2,0,8,0,4,6,8,1,10,4,2,9]
print(bin_sort(A,10)) # [0,0,1,2,2,3,4,4,5,6,8,8,9,10]
