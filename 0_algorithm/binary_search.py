# binary search (O(log(r-l)))
def bisect(l,r,f,left=True):
    """
    l,r: int (l<r)
    f: {l,...,r} to {False,True}
    if left: f satisfies that there uniquely exists d such that iff i<=d then f(i)
    else: iff i>=d then f(i) is True
    return d such as those above
    """
    if left and f(r): return r
    elif left and (not f(l)): return l-1
    elif (not left) and f(l): return l
    elif (not left) and (not f(r)): return r+1
    while(True):
        if r-l<=1: # terminate
            if (not left)^f(l): return l if left else l+1
            else: return h if left else l+1
        h=(l+r)//2
        if (not left)^f(h): l=h
        else: r=h

#%%
print(bisect(-4,10,lambda x:x>5,left=False))
