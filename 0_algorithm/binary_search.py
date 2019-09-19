# binary search (O(log(r-l)))
def bisect(l,r,f,left=True):
    """
    l,r: int (l<r)
    f: {l,...,r} to {False,True}
    if left: f satisfies that there uniquely exists d such that iff i<=d then f(i)
    else: iff i>=d then f(i) is True
    return d such as those above
    """
    assert r>l
    if (not left)^f(r): return r if left else r+1
    elif left^f(l): return l-1 if left else l
    while(True):
        if r-l<=1: return l if f(l) else r
        h=(l+r)//2
        if (not left)^f(h): l=h
        else: r=h

#%%
print(bisect(-4,10,lambda x:x>5.7,left=False))

#%%
print(bisect(-4,10,lambda x:x>5,left=False))
