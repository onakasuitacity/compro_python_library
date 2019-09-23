# n進数
def nsin(x, n):
    if(int(x/n)):
        return nsin(int(x/n),n)+str(x%n)
    return str(x)

# Eratosthenes Sieve (O(nloglogn))
def prime(n,is_prime=True):
    """
    n: positive integer
    if is_prime: return n is prime
    else: return list of prime <= n 
    """
    if n<=1: return False if is_prime else []
    S=[1]*(n+1)
    S[0]=0; S[1]=0
    for i in range(2,n):
        if S[i]==0: continue
        for j in range(2*i,n+1,i):
            S[j]=0
    if is_prime: return bool(S[n])
    else: return [p for p in range(n+1) if S[p]]

# prime factorization (O(sqrt(N)))
def trial_division(n):
    factor=[]
    sqrt=int(n**.5)+1 # sqrt=ceil(sqrt(n))
    for num in range(2,sqrt):
        while n % num == 0:
            n //= num
            factor.append(num)
    if n==1: return factor
    else: return factor+[n]

# divisors (O(sqrt(N)))
def divisors(n):
    S,T=[],[]
    for i in range(1,int(n**.5)+1):
        if n%i==0:
            S.append(i)
            T.append(n//i)
    T.reverse()
    return S+T if S[-1]!=T[0] else S+T[1:]

# aのZ/mZでのinverse
# https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a
def modinv(a,m):
    b,u,v=m,1,0
    while(b):
        t=a//b
        a-=t*b; a,b=b,a
        u-=t*v; u,v=v,u
    u%=m
    if u<0: u+=m
    return u

# power set
# https://qiita.com/hrsma2i/items/d98f9b1fceeb23d67eef
from itertools import chain,combinations
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

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

# matrix multiple (ijk-algorithm)
def mat_mul(A,B):
    assert len(A[0])==len(B)
    m=len(A)
    n=len(B)
    l=len(B[0])
    C=[[0]*l for _ in range(m)]
    for i in range(m):
        for j in range(l):
            for k in range(n):
                C[i][j]+=A[i][k]*B[k][j]
    return C
