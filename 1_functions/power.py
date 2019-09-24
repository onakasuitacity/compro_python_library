# Exponential (O(logp))
def power(b,p,f):
    """
    b: object (base)
    p: positive int (multiplier)
    f: multiple function
    return: f^p(b)
    """
    if not isinstance(p,int): raise ValueError("multiplier must be int")
    elif p<=0: raise ValueError("multiplier must be positive.")
    logp=p.bit_length()
    S=[0]*logp
    S[0]=b
    res='$'
    for i in range(logp):
        if i!=logp-1: S[i+1]=f(S[i],S[i])
        if p&(1<<i):
            if res=='$': res=S[i]
            else: res=f(res,S[i])
    return res
