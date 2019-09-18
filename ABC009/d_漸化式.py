# https://atcoder.jp/contests/abc009/tasks/abc009_4
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
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
                    C[i][j]^=A[i][k]&B[k][j]
        return C

    k,m=map(int,input().split())
    vec=list(map(lambda x:[int(x)],input().split()))
    if m<=k:
        print(vec[m-1][0])
        return
    vec=vec[::-1]
    mat=[0]*k
    mat[0]=list(map(int,input().split()))
    for i in range(k-1):
        # &のunitは-1
        mat[i+1]=[-1 if j==i else 0 for j in range(k)] # kxk
    P=power(mat,m-k,mat_mul)
    vec=mat_mul(P,vec)
    print(vec[0][0])
resolve()
