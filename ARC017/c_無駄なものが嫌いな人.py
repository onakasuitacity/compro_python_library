# https://atcoder.jp/contests/arc017/tasks/arc017_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7 # 998244353
input=lambda:sys.stdin.readline().rstrip()
from collections import defaultdict
def resolve():
    n,x=map(int,input().split())
    W=[int(input()) for _ in range(n)]

    # 半分全列挙
    X=W[:n//2]; Y=W[n//2:]

    # Y の部分和を全列挙して、counterを用意する
    D=defaultdict(int)
    D[0]+=1
    now=0
    for i in range(1,1<<((n+1)//2)):
        code=i^(i>>1)
        lsb=(i&(-i))
        t=lsb.bit_length()-1
        if(code&lsb): now+=Y[t]
        else: now-=Y[t]
        D[now]+=1

    # X の部分和に対して、和を x にする個数を足し合わせる
    ans=D[x]
    now=0
    for i in range(1,1<<(n//2)):
        code=i^(i>>1)
        lsb=(i&(-i))
        t=lsb.bit_length()-1
        if(code&lsb): now+=X[t]
        else: now-=X[t]
        ans+=D[x-now]

    print(ans)
resolve()
