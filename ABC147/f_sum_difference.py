# https://atcoder.jp/contests/abc147/tasks/abc147_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from collections import defaultdict
def resolve():
    n,a,d=map(int,input().split())
    if(d==0):
        if(a==0): print(1)
        else: print(n+1)
        return
    if(d<0): a,d=-a,-d

    D=defaultdict(list)
    for k in range(n+1):
        L=k*a+k*(k-1)*d//2
        R=k*a+k*(2*n-k-1)*d//2
        r=L%d
        D[r].append((L//d,0))
        D[r].append((R//d,1))

    ans=0
    for arr in D.values():
        arr.sort()
        over=0
        now=0
        for v,q in arr:
            if(q==0):
                if(not over): now=v
                over+=1
            else:
                over-=1
                if(not over): ans+=v-now+1

    print(ans)
resolve()
