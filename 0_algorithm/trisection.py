def trisection(l,r,f,convex=True,discrete=True):
    eps=2 if(discrete) else 10**-12
    while(r-l>eps):
        d=(r-l)//3 if(discrete) else (r-l)/3
        h1=l+d; h2=r-d
        if((f(h1)>=f(h2))^convex): r=h2
        else: l=h1
    if(discrete):
        if(convex): return min([(f(l),l),(f(l+1),l+1),(f(r),r)])[1]
        else: return max([(f(l),l),(f(l+1),l+1),(f(r),r)])[1]
    else:
        if(convex): return min([(f(l),l),(f(r),r)])[1]
        else: return max([(f(l),l),(f(r),r)])[1]

#%% example
f=lambda x:-(x-3)**2+4
print(trisection(-100,100,f,convex=False,discrete=True))
