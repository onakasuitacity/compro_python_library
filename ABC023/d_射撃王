# https://atcoder.jp/contests/abc023/tasks/abc023_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def bin_sort(A,n_min=None,n_max=None):
    """
    A: list of integer
    n_min: minimum of A
    n_max: maximum of A
    """
    if n_min is None: n_min=min(A)
    if n_max is None: n_max=max(A)
    bin=[0]*(n_max-n_min+1)
    for a in A: bin[a]+=1
    B=[]
    for i in range(n_min,n_max+1): B+=[i]*bin[i]
    return B

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

def resolve():
    n=int(input())
    H=[0]*n; S=[0]*n
    for i in range(n):
        H[i],S[i]=map(int,input().split())
    h=max(H); s=max(S)
    # 0<=x<=h+nsに対して、可能かどうかをbooleanで返す関数を作る
    def judge(x):
        T=[0]*n
        for i in range(n):
            t=min((x-H[i])//S[i],n-1)
            if t<0: return False
            T[i]=t
        T=bin_sort(T,0,n-1)
        return all(i<=T[i] for i in range(n))
    print(bisect(0,h+n*s,judge,left=False))
resolve()
