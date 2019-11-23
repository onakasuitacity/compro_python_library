# https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()

prod=True
N=5
ANS="BRRBBRBRBR"

def ask(A): # A:list-like
    print("? {}".format(' '.join(map(str,A))))
    sys.stdout.flush()
    if(prod): return input()
    else:
        cnt=0
        for a in A:
            cnt+=ANS[a-1]=='R'
        return "Red" if(cnt>(N-cnt)) else "Blue"

def resolve():        
    n=int(input()) if(prod) else N

    # 二分法でRとBの境目を一つ見つける
    l=1; r=n+1
    lcol=ask(range(1,1+n))
    rcol="Red" if(lcol=="Blue") else "Blue"
    while(r-l>1):
        h=(l+r)//2
        hcol=ask(range(h,h+n))
        if(lcol==hcol): l=h
        else: r=h

    res=[None]*(2*n+1) # 1-indexed
    idx=l
    res[idx]=lcol[0]
    res[idx+n]=rcol[0]

    for i in range(1,idx):
        A=[i]+list(range(idx+1,idx+n))
        res[i]=ask(A)[0]
    for i in range(idx+n+1,2*n+1):
        A=list(range(idx+1,idx+n))+[i]
        res[i]=ask(A)[0]
    for i in range(idx+1,idx+n):
        A=list(range(1,idx))+[i]+list(range(idx+n+1,2*n+1))
        res[i]=ask(A)[0]
    print("! {}".format(''.join(res[1:])))
resolve()
