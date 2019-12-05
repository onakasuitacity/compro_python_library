# https://atcoder.jp/contests/abc007/tasks/abc007_4
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from itertools import product,chain
def resolve():
    A,B=map(lambda x:x.zfill(19),input().split())
    dp=[[0]*2 for _ in range(2)]
    dp[0][0]=1

    for a,b in zip(A,B):
        a=int(a); b=int(b)
        ndp=[[0]*2 for _ in range(2)]
        for d,mt,lt in product(range(10),range(2),range(2)):
            if(d==4 or d==9): continue
            if((not mt) and (a>d)): continue
            if((not lt) and (d>b)): continue
            ndp[max(mt,a<d)][max(lt,d<b)]+=dp[mt][lt]
        dp=ndp

    print(int(B)-int(A)+1-sum(chain.from_iterable(dp)))
resolve()
