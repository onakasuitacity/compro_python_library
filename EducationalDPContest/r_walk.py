# https://atcoder.jp/contests/dp/tasks/dp_r
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
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
                C[i][j]%=MOD
    return C

def resolve():
    n,k=map(int,input().split())
    A=[list(map(int,input().split())) for _ in range(n)]
    dp=[[1]]*n
    A=power(A,k,mat_mul)
    dp=mat_mul(A,dp)
    res=0
    for i in range(n): res+=dp[i][0]
    print(res%MOD)
resolve()
