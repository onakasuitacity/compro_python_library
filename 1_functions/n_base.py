def n_base(x,n):
    if(x//n): return n_base(x//n,n)+str(x%n)
    else: return str(x)
