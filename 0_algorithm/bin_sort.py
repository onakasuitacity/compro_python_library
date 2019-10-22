# bin sort O(range(A)+len(A))
# https://engineeringnote.hateblo.jp/entry/python/algorithm-and-data-structures/bin_sort
def bin_sort(A,n_min=None,n_max=None):
    if(n_min is None): n_min=min(A)
    if(n_max is None): n_max=max(A)
    bin=[0]*(n_max-n_min+1)
    for a in A: bin[a-n_min]+=1
    B=[]
    for i in range(n_min,n_max+1): B+=[i]*bin[i-n_min]
    return B

# example
A=[3,-5,8,2,3,8,-4,-3,0,-3,5]
print(bin_sort(A)) # [-5,-4,-3,-3,0,2,3,3,5,8,8]
